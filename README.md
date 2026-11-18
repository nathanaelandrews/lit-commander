# lit-commander

Collects new papers each night for a daily literature scan.

A GitHub Actions job (`.github/workflows/collect.yml`) runs `collector.py` at 02:37 UTC. It pulls:

- **Journals** from Crossref (one query per journal, by ISSN, on the date the DOI was registered) and from PubMed (by ISSN, on the date the record entered PubMed; adds abstracts and affiliations).
- **Preprints** from the bioRxiv and medRxiv API, filtered to the categories in `config.json`. New versions of preprints first posted more than 30 days ago are dropped.

Each run looks back `lookback_days` (default 3) and skips anything collected on an earlier day (`state/seen.json`), so late-indexed papers are still picked up once and nothing repeats.

## Output

- `candidates/YYYY-MM-DD.json`: full records plus per-source status.
- `candidates/YYYY-MM-DD.md`: compact digest. Keyword hits (core/secondary, then disease-only) come with abstracts; everything else is one line each.
- `candidates/latest.json` and `candidates/latest.md`: copies of the newest run.

Raw URL for the digest: `https://raw.githubusercontent.com/nathanaelandrews/lit-commander/main/candidates/latest.md`

## Changing what is collected

Edit `config.json`: journals (name and ISSNs), preprint categories, keyword lists, look-back window. Keywords containing a backslash are treated as case-sensitive regular expressions (e.g. `\\bALS\\b`); all others are case-insensitive substrings.

## Running by hand

Actions tab → *Collect candidates* → *Run workflow*. Optionally set a longer look-back to backfill.

Optional: add an `NCBI_API_KEY` repository secret to raise PubMed's rate limit. Not needed at this volume.
