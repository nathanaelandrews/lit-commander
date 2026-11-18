"""Daily literature collector.

Pulls new papers from Crossref (journals), PubMed (journals, with abstracts and
affiliations) and the bioRxiv/medRxiv API, removes anything collected on an
earlier day, and writes:

    candidates/YYYY-MM-DD.json   full records
    candidates/YYYY-MM-DD.md     compact digest for the morning scan
    candidates/latest.json/.md   copies of the newest run
    state/seen.json              DOIs already collected (for de-duplication)

Only the Python standard library is used. Configuration lives in config.json.
"""

import datetime as dt
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USER_AGENT = "lit-commander/1.0 (+https://github.com/nathanaelandrews/lit-commander)"
TODAY = dt.datetime.now(dt.timezone.utc).date()

# Titles that are never research content
JUNK_TITLE = re.compile(
    r"^(author correction|publisher correction|correction|erratum|corrigendum|retraction|"
    r"retracted|expression of concern|editorial expression|reply to|matters arising)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------- HTTP helpers

def http_get(url, data=None, retries=3, timeout=60):
    """GET (or POST when data is given) with a few retries; returns bytes."""
    body = urllib.parse.urlencode(data).encode() if data else None
    last_error = None
    for attempt in range(retries):
        request = urllib.request.Request(url, data=body, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"{url[:120]}: {last_error}")


def get_json(url, data=None):
    return json.loads(http_get(url, data))


# ---------------------------------------------------------------- text helpers

def strip_tags(text):
    """Remove JATS/HTML tags and collapse whitespace."""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def normalise_doi(doi):
    doi = (doi or "").strip().lower()
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)


def compile_keywords(keyword_config):
    """Keywords containing a backslash are regexes (case-sensitive); others are plain, case-insensitive."""
    compiled = {}
    for tier, words in keyword_config.items():
        patterns = []
        for word in words:
            if "\\" in word:
                patterns.append(re.compile(word))
            else:
                patterns.append(re.compile(re.escape(word), re.IGNORECASE))
        compiled[tier] = patterns
    return compiled


def keyword_hits(item, compiled_keywords):
    text = f"{item['title']} {item.get('abstract', '')}"
    return [tier for tier, patterns in compiled_keywords.items()
            if any(p.search(text) for p in patterns)]


def make_item(**fields):
    """Common record shape for every source."""
    item = {
        "doi": "", "title": "", "journal": "", "date": "", "source": "",
        "authors": [], "first_author": "", "last_author": "", "last_author_affiliation": "",
        "corresponding_author": "", "corresponding_institution": "",
        "abstract": "", "url": "", "type": "", "version": "",
    }
    item.update(fields)
    if item["authors"]:
        item["first_author"] = item["first_author"] or item["authors"][0]
        item["last_author"] = item["last_author"] or item["authors"][-1]
    if item["doi"] and not item["url"]:
        item["url"] = f"https://doi.org/{item['doi']}"
    return item


# ---------------------------------------------------------------- Crossref

def crossref_author_name(author):
    if "family" in author:
        return f"{author.get('given', '')} {author['family']}".strip()
    return author.get("name", "")


def crossref_date(record):
    parts = (record.get("published") or record.get("created") or {}).get("date-parts", [[None]])[0]
    return "-".join(f"{p:02d}" for p in parts if p) if parts and parts[0] else ""


def fetch_crossref_journal(journal, date_from, date_to):
    """All journal articles whose DOI was registered in the window, for one journal."""
    filters = [f"issn:{issn}" for issn in journal["issn"]]
    filters += [f"from-created-date:{date_from}", f"until-created-date:{date_to}", "type:journal-article"]
    params = {
        "filter": ",".join(filters),
        "rows": 1000,
        "select": "DOI,title,author,container-title,created,published,abstract,type,URL",
    }
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    records = get_json(url)["message"]["items"]

    items = []
    for record in records:
        title = strip_tags(" ".join(record.get("title") or []))
        authors_raw = [a for a in record.get("author", []) if crossref_author_name(a)]
        authors = [crossref_author_name(a) for a in authors_raw]
        last_affiliation = ""
        if authors_raw:
            affiliations = authors_raw[-1].get("affiliation") or []
            last_affiliation = "; ".join(a.get("name", "") for a in affiliations)
        items.append(make_item(
            doi=normalise_doi(record.get("DOI")),
            title=title,
            journal=journal["name"],
            date=crossref_date(record),
            source="crossref",
            authors=authors,
            last_author_affiliation=last_affiliation,
            abstract=strip_tags(record.get("abstract")),
            type=record.get("type", ""),
        ))
    return items


# ---------------------------------------------------------------- PubMed

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
PUBMED_EXCLUDED_TYPES = {
    "Comment", "Editorial", "News", "Published Erratum", "Retraction of Publication",
    "Retracted Publication", "Expression of Concern", "Letter", "Biography", "Interview",
    "Portrait", "Newspaper Article",
}


def pubmed_params(extra):
    params = {"db": "pubmed", "tool": "lit-commander"}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    params.update(extra)
    return params


def pubmed_search(journals, date_from, date_to):
    """Search by ISSN and Entrez date (date the record entered PubMed). POST avoids URL-length limits."""
    issn_terms = " OR ".join(f'"{issn}"[is]' for j in journals for issn in j["issn"])
    term = f'({issn_terms}) AND ("{date_from.replace("-", "/")}"[edat] : "{date_to.replace("-", "/")}"[edat])'
    result = get_json(f"{EUTILS}/esearch.fcgi",
                      pubmed_params({"term": term, "retmax": 2000, "retmode": "json"}))
    return result["esearchresult"]["idlist"]


def pubmed_article_to_item(article):
    citation = article.find("MedlineCitation")
    art = citation.find("Article")

    publication_types = {pt.text for pt in art.findall("PublicationTypeList/PublicationType")}
    if publication_types & PUBMED_EXCLUDED_TYPES:
        return None

    authors, affiliations = [], []
    for author in art.findall("AuthorList/Author"):
        if author.find("LastName") is not None:
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName')}".strip()
        elif author.find("CollectiveName") is not None:
            name = author.findtext("CollectiveName")
        else:
            continue
        authors.append(name)
        affiliations.append("; ".join(a.text or "" for a in author.findall("AffiliationInfo/Affiliation")))

    abstract_parts = []
    for part in art.findall("Abstract/AbstractText"):
        label = part.get("Label")
        text = "".join(part.itertext()).strip()
        abstract_parts.append(f"{label}: {text}" if label else text)

    doi = ""
    for article_id in article.findall("PubmedData/ArticleIdList/ArticleId"):
        if article_id.get("IdType") == "doi":
            doi = normalise_doi(article_id.text)

    date_node = art.find("ArticleDate")
    if date_node is not None:
        date = "-".join(date_node.findtext(k, "") for k in ("Year", "Month", "Day"))
    else:
        date = " ".join(art.findtext(f"Journal/JournalIssue/PubDate/{k}", "") for k in ("Year", "Month", "Day")).strip()

    pmid = citation.findtext("PMID")
    return make_item(
        doi=doi,
        title="".join(art.find("ArticleTitle").itertext()).strip() if art.find("ArticleTitle") is not None else "",
        journal=art.findtext("Journal/ISOAbbreviation") or art.findtext("Journal/Title", ""),
        date=date,
        source="pubmed",
        authors=authors,
        last_author_affiliation=affiliations[-1] if affiliations else "",
        abstract=" ".join(abstract_parts),
        url=f"https://doi.org/{doi}" if doi else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        type="; ".join(sorted(publication_types)),
        pmid=pmid,
    )


def fetch_pubmed(journals, date_from, date_to):
    pmids = pubmed_search(journals, date_from, date_to)
    items = []
    for start in range(0, len(pmids), 200):
        batch = pmids[start:start + 200]
        xml_bytes = http_get(f"{EUTILS}/efetch.fcgi",
                             pubmed_params({"id": ",".join(batch), "retmode": "xml"}))
        for article in ET.fromstring(xml_bytes).findall("PubmedArticle"):
            item = pubmed_article_to_item(article)
            if item:
                items.append(item)
        time.sleep(0.5)
    return items


# ---------------------------------------------------------------- bioRxiv / medRxiv

def doi_posting_date(doi):
    """bioRxiv/medRxiv DOIs embed the first-posting date, e.g. 10.1101/2025.02.18.123456."""
    match = re.search(r"/(\d{4})\.(\d{2})\.(\d{2})\.", doi)
    if not match:
        return None
    try:
        return dt.date(*map(int, match.groups()))
    except ValueError:
        return None


def fetch_preprints(server, categories, date_from, date_to, max_age_days):
    """All posts in the window, filtered to the given categories; drops revisions of old preprints."""
    wanted = {c.lower() for c in categories}
    oldest_allowed = TODAY - dt.timedelta(days=max_age_days)
    items, cursor = [], 0
    while True:
        page = get_json(f"https://api.biorxiv.org/details/{server}/{date_from}/{date_to}/{cursor}/json")
        records = page.get("collection", [])
        for record in records:
            if record.get("category", "").lower() not in wanted:
                continue
            doi = normalise_doi(record.get("doi"))
            first_posted = doi_posting_date(doi)
            if first_posted and first_posted < oldest_allowed:
                continue  # a new version of an old preprint
            authors = [a.strip() for a in record.get("authors", "").split(";") if a.strip()]
            items.append(make_item(
                doi=doi,
                title=strip_tags(record.get("title")),
                journal=server,
                date=record.get("date", ""),
                source=server,
                authors=authors,
                corresponding_author=record.get("author_corresponding", ""),
                corresponding_institution=record.get("author_corresponding_institution", ""),
                abstract=strip_tags(record.get("abstract")),
                type=record.get("category", ""),
                version=record.get("version", ""),
            ))
        message = (page.get("messages") or [{}])[0]
        total = int(message.get("total", 0) or 0)
        cursor += len(records)
        if not records or cursor >= total:
            break
        time.sleep(0.5)
    return items


# ---------------------------------------------------------------- merge, de-duplicate

def item_key(item):
    """DOI when present, otherwise PubMed ID, otherwise the lower-cased title."""
    if item["doi"]:
        return item["doi"]
    if item.get("pmid"):
        return f"pmid:{item['pmid']}"
    return item["title"].lower()


def merge_items(item_lists):
    """Merge records with the same DOI, filling empty fields (e.g. PubMed abstract into a Crossref record)."""
    merged, order = {}, []
    for items in item_lists:
        for item in items:
            key = item_key(item)
            if key not in merged:
                merged[key] = item
                order.append(key)
                continue
            existing = merged[key]
            existing["source"] = ",".join(sorted(set(existing["source"].split(",") + [item["source"]])))
            for field, value in item.items():
                if value and not existing.get(field):
                    existing[field] = value
            # Keep the longer abstract (PubMed is usually fuller than Crossref)
            if len(item["abstract"]) > len(existing["abstract"]):
                existing["abstract"] = item["abstract"]
    return [merged[k] for k in order]


def load_seen():
    path = ROOT / "state" / "seen.json"
    return json.loads(path.read_text()) if path.exists() else {}


def save_seen(seen, retention_days):
    cutoff = (TODAY - dt.timedelta(days=retention_days)).isoformat()
    kept = {doi: day for doi, day in seen.items() if day >= cutoff}
    path = ROOT / "state" / "seen.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(kept, indent=0, sort_keys=True))


# ---------------------------------------------------------------- output

def format_item_full(item, abstract_chars):
    lines = [f"### {item['title']}",
             f"- {item['journal']} | {item['date']} | {item['url']}"]
    if item["version"] and str(item["version"]) != "1":
        lines[-1] += f" | version {item['version']}"
    lines.append(f"- First: {item['first_author']} | Last: {item['last_author']}"
                 + (f" ({item['last_author_affiliation'][:200]})" if item["last_author_affiliation"] else ""))
    if item["corresponding_author"]:
        lines.append(f"- Corresponding: {item['corresponding_author']} ({item['corresponding_institution']})")
    lines.append(f"- Tags: {', '.join(item['hits']) or 'none'} | n_authors: {len(item['authors'])}")
    abstract = item["abstract"]
    if abstract:
        lines.append(abstract[:abstract_chars] + ("..." if len(abstract) > abstract_chars else ""))
    else:
        lines.append("(no abstract in metadata)")
    return "\n".join(lines)


def format_item_short(item):
    return f"- {item['journal']} | {item['title']} | last: {item['last_author']} | {item['url']}"


def write_digest(items, source_status, windows, path):
    tiers = {
        "core_or_secondary": [i for i in items if {"core", "secondary"} & set(i["hits"])],
        "disease_only": [i for i in items if i["hits"] == ["disease"]],
        "other": [i for i in items if not i["hits"]],
    }
    out = [f"# Candidates collected {TODAY.isoformat()}",
           "",
           f"Windows: journals {windows['journals']}, preprints {windows['preprints']}. "
           "Items collected on earlier days are excluded.",
           "",
           "## Source status",
           ""]
    for name, status in source_status.items():
        out.append(f"- {name}: {status['status']}, {status['count']} items"
                   + (f" | ERROR: {status['error']}" if status.get("error") else ""))
    out += ["", f"## Keyword hits: core / secondary ({len(tiers['core_or_secondary'])})", ""]
    out += [format_item_full(i, 1200) + "\n" for i in tiers["core_or_secondary"]]
    out += [f"## Keyword hits: disease only ({len(tiers['disease_only'])})", ""]
    out += [format_item_full(i, 500) + "\n" for i in tiers["disease_only"]]
    out += [f"## No keyword hits ({len(tiers['other'])})", ""]
    out += [format_item_short(i) for i in tiers["other"]]
    path.write_text("\n".join(out) + "\n")


# ---------------------------------------------------------------- main

def run_source(name, function, source_status, *args):
    """Run one source; record success or failure without stopping the whole collection."""
    try:
        items = function(*args)
        source_status[name] = {"status": "ok", "count": len(items)}
        return items
    except Exception as error:  # noqa: BLE001 - any failure is logged and reported, not hidden
        source_status[name] = {"status": "FAILED", "count": 0, "error": str(error)[:300]}
        print(f"[{name}] FAILED: {error}", file=sys.stderr)
        return []


def main():
    config = json.loads((ROOT / "config.json").read_text())
    lookback = int(os.environ.get("LOOKBACK_DAYS") or config["lookback_days"])
    date_from = (TODAY - dt.timedelta(days=lookback)).isoformat()
    date_to = TODAY.isoformat()
    preprint_to = (TODAY - dt.timedelta(days=1)).isoformat()

    source_status, item_lists = {}, []

    # Journals via Crossref, one request per journal so a bad ISSN shows up as a zero count
    for journal in config["journals"]:
        item_lists.append(run_source(f"crossref:{journal['name']}", fetch_crossref_journal,
                                     source_status, journal, date_from, date_to))
        time.sleep(0.3)

    # Journals via PubMed (adds abstracts and affiliations, catches anything Crossref missed)
    item_lists.append(run_source("pubmed", fetch_pubmed, source_status,
                                 config["journals"], date_from, date_to))

    # Preprints
    for server in ("biorxiv", "medrxiv"):
        item_lists.append(run_source(server, fetch_preprints, source_status, server,
                                     config["preprint_categories"][server], date_from, preprint_to,
                                     config["preprint_max_age_days"]))

    all_items = merge_items(item_lists)
    all_items = [i for i in all_items if i["title"] and not JUNK_TITLE.search(i["title"])]

    # Drop anything collected on an earlier day
    seen = load_seen()
    new_items = [i for i in all_items if item_key(i) not in seen]
    for item in new_items:
        seen[item_key(item)] = TODAY.isoformat()

    compiled_keywords = compile_keywords(config["keywords"])
    for item in new_items:
        item["hits"] = keyword_hits(item, compiled_keywords)

    windows = {"journals": f"{date_from} to {date_to}", "preprints": f"{date_from} to {preprint_to}"}
    payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "windows": windows,
        "sources": source_status,
        "n_items": len(new_items),
        "items": new_items,
    }

    out_dir = ROOT / "candidates"
    out_dir.mkdir(exist_ok=True)
    for stem in (TODAY.isoformat(), "latest"):
        (out_dir / f"{stem}.json").write_text(json.dumps(payload, indent=1, ensure_ascii=False))
        write_digest(new_items, source_status, windows, out_dir / f"{stem}.md")
    save_seen(seen, config["seen_retention_days"])

    failed = [n for n, s in source_status.items() if s["status"] != "ok"]
    print(f"{len(new_items)} new items; failed sources: {failed or 'none'}")


if __name__ == "__main__":
    main()
