# Candidates collected 2026-11-20

Windows: journals 2026-11-17 to 2026-11-20, preprints 2026-11-17 to 2026-11-19. Items collected on earlier days are excluded.

## Source status (records returned by each source in the latest run, before de-duplication)

- crossref:Nature: ok, 76 items
- crossref:Science: ok, 38 items
- crossref:Cell: ok, 8 items
- crossref:Nature Methods: ok, 7 items
- crossref:Nature Biotechnology: ok, 2 items
- crossref:Nature Genetics: ok, 5 items
- crossref:Nature Medicine: ok, 5 items
- crossref:Nature Communications: ok, 106 items
- crossref:Science Advances: ok, 44 items
- crossref:Nature Cancer: ok, 4 items
- crossref:Nature Neuroscience: ok, 4 items
- crossref:Cell Genomics: ok, 0 items
- crossref:Cell Systems: ok, 3 items
- crossref:Molecular Cell: ok, 7 items
- crossref:Cancer Cell: ok, 1 items
- crossref:Neuron: ok, 2 items
- crossref:Am J Hum Genet: ok, 1 items
- crossref:Genome Biology: ok, 14 items
- crossref:Genome Research: ok, 0 items
- crossref:Cancer Discovery: ok, 4 items
- crossref:NEJM: ok, 22 items
- pubmed: ok, 243 items
- biorxiv: ok, 466 items
- medrxiv: ok, 25 items

## Keyword hits: core / secondary (42)

### Space-map: 3D single-cell atlas reconstruction from serial sections
- Nature Methods | 2026-11-19 | https://doi.org/10.1038/s41592-026-03310-8
- First: Rongduo Han | Last: Michael P. Snyder
- Tags: core | n_authors: 17
Abstract High-resolution three-dimensional (3D) tissue atlases promise to link cellular architecture to tissue function, but assembling them from serial sections containing millions of cells remains challenging. Here we present Space-map, an accurate and efficient method for reconstructing 3D tissue models from high-content spatial molecular profiles. Space-map combines multiscale feature matching with large deformation diffeomorphic metric mapping to automate global alignment across serial sections while preserving local microanatomy. We generate spatial transcriptomics (Xenium; ~2.7 million cells) and proteomics (CODEX; ~4.8 million cells) datasets from serial sections to build 3D models of a colon polyp and healthy intestinal tissues. These models reveal cell-type heterogeneity in the polyp and preserved crypt and glandular architecture and mucosal-cavity continuity in healthy intestines. Benchmarking on our own and publicly available datasets demonstrates that Space-map achieves substantially higher registration accuracy and up to a tenfold speedup over existing methods, supporting its use as a robust framework for constructing 3D human tissue atlases at single-cell resolution.

### Optimizing phenotype scale improves genetic analyses in large-scale biobanks
- Nature Genetics | 2026-11-19 | https://doi.org/10.1038/s41588-026-02826-1
- First: Zhenhong Huang | Last: Andy Dahl
- Tags: secondary | n_authors: 3
Abstract Large-scale biobanks have enabled increasingly complicated genetic analyses across thousands of phenotypes. However, studies rarely consider the appropriateness of the phenotype scale, which can drastically affect inference on genetic architecture. Here we introduce SIQReg, which learns a data-driven phenotype scale by minimizing heterogeneity across phenotype quantiles. Across 25 UK Biobank complex traits, SIQReg rejects the default scale for 24. Generally, SIQReg scales lie between default and logarithmic, indicating that traits are neither purely additive nor purely multiplicative. SIQReg improves both nonadditive and additive genetic analyses. It eliminates most nonadditive signals, including 97% of variance quantitative trait loci, indicating that they may be scale-induced, while preserving biologically plausible nonadditive signals. It simultaneously improves power for additive signals, increasing identification of genome-wide association loci and transcriptome-wide association genes by 11% and 13%, respectively, improving polygenic prediction accuracy by 10%, and identifying 50% more high-risk individuals. These gains are replicated across ancestry groups. Our resul...

### Benchmarking computational tools for locus-specific analysis of transposable elements in single-cell RNA-seq datasets
- Genome Biology | 2026-11-19 | https://doi.org/10.1186/s13059-026-04349-8
- First: Veronica Finazzi | Last: Antonio Scialdone
- Tags: core | n_authors: 3
Abstract Background Transposable elements (TEs) are increasingly recognized as regulators of gene expression and cellular identity. Single-cell RNA-sequencing (scRNA-seq) enables the analysis of their transcription at cellular resolution, but the repetitive nature of TEs and their frequent overlap with genes create substantial mapping ambiguity. Although several tools quantify TE expression, few support locus-specific analysis, and their performance in single-cell data has not been systematically evaluated. Results We present a comprehensive, scalable benchmarking framework written in Snakemake for locus-level TE quantification in short-read scRNA-seq data, combining real datasets with simulations that provide read-level ground truth. Our simulations show that sequence-diverged insertions can be quantified with relatively high accuracy, whereas young TEs remain difficult to resolve due to unreliable assignment of multi-mapping reads. We observe pronounced family-specific biases and identify gene-TE disambiguation as a major unresolved challenge. Across the evaluated methods, incorporating multi-mapping reads generally increased false-positive calls without substantially improving l...

### Adding layers of information to scRNA-seq data using pre-trained language models
- Genome Biology | 2026-11-19 | https://doi.org/10.1186/s13059-026-04353-y
- First: Sonia Maria Krißmer | Last: Maren Hackenberg
- Tags: core | n_authors: 6
Abstract Pre-trained language models promise to enrich single-cell analyses with contextual information from large biomedical text corpora, but it remains unclear how to optimally align this knowledge with quantitative single-cell RNA sequencing (scRNA-seq) data. To address this, we construct text-based training datasets from both scRNA-seq data and biomedical literature targeted to the experimental setting at hand. We then fine-tune lightweight encoder-only biomedical language models to learn a shared, literature-enriched representation. Controlled evaluations across immune and developmental datasets show that this representation preserves cell identity while adding robust and interpretable contextual layers of functional, disease-associated, and developmental information to single-cell analysis workflows.

### SPiCe: integrative spatial modelling of cellular plasticity using graph neural networks and geostatistics
- Genome Biology | 2026-11-19 | https://doi.org/10.1186/s13059-026-04350-1
- First: Eloise Withnell | Last: Maria Secrier
- Tags: core, disease | n_authors: 3
Abstract Cellular plasticity, the ability of cells to change phenotype in response to intrinsic and environmental cues, is central to development and disease, yet remains difficult to quantify. We present SPiCe, a framework that integrates graph neural networks and spatial regression models to predict and explain cell state variation in spatial transcriptomics data. Applied to epithelial-mesenchymal plasticity (EMP) in breast cancer, SPiCe shows that mesenchymal states are stabilised by copy number alterations and microenvironmental cues, whereas hybrid states remain unpredictable, and uncovers long-range myofibroblast influences on EMP. Together, these analyses provide a framework for quantifying cellular plasticity and its spatial determinants.

### Joint-Cabernet enables scalable single-cell joint profiling of transcriptomes with DNA methylation and hydroxymethylation in the brain
- Genome Biology | 2026-11-19 | https://doi.org/10.1186/s13059-026-04351-0
- First: Yali Bai | Last: Yunlong Cao
- Tags: core | n_authors: 17
(no abstract in metadata)

### scDCF: detecting disease-associated cells from scRNA-seq using GWAS findings and healthy reference panels
- Genome Biology | 2026-11-19 | https://doi.org/10.1186/s13059-026-04347-w
- First: Caicai Zhang | Last: Wanling Yang
- Tags: core, secondary | n_authors: 9
(no abstract in metadata)

### Silk fibroin intrinsically activates Ccl27⁺ migratory-paracrine keratinocytes to orchestrate epidermal-dermal crosstalk for regenerative wound healing.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78745-w
- First: Yue Zhu | Last: Wei Zhang (Department of Orthopedics, Nantong First People's Hospital, School of Medicine, Southeast University, Nantong, China. zhang.wei@seu.edu.cn.; School of Medicine, Southeast University, Nanjing, China. z)
- Tags: core | n_authors: 14
Rapid and functional skin wound healing remains a major clinical challenge, while current biomaterial-based therapies largely serve as passive scaffolds or delivery vehicles. Whether biomaterials possess intrinsic bioactivities that instruct endogenous regenerative programs remains unclear. Here, independent of bulk structural/mechanical cues or exogenous biomolecules, we show that silk fibroin (SF), a clinically approved biomaterial, intrinsically programs keratinocytes into a Ccl27⁺ migratory-paracrine pro-regenerative state that coordinates epidermal-dermal crosstalk to drive regenerative wound healing. Integrated scRNA-seq, proteomics, and genetic perturbation reveal that SF engages keratinocyte ITGA2 to activate PI3K-Akt signaling and relieve P53-mediated Ccl27 repression. Elevated Ccl27 enhances keratinocyte migration and re-epithelialization, while its secretion from SF-activated keratinocytes promotes fibroblast proliferation and dermal remodeling, collectively enabling wound closure and appendage reconstruction. Keratinocyte-specific Ccl27 knockdown largely abrogates SF-mediated regeneration in vivo. These findings uncover the intrinsic bioactivity of SF and establish biom...

### Spatially resolved host and microbiota RNA profiling in the mouse gut using microDBiT.
- Nature Communications | 2026-10-19 | https://doi.org/10.1038/s41467-026-78852-8
- First: Bo Tao | Last: Yang Liu (Department of Pathology, Yale School of Medicine, New Haven, CT, USA. yang.liu.yl2224@yale.edu.; Department of Neurology, Yale School of Medicine, New Haven, CT, USA. yang.liu.yl2224@yale.edu.; Yale C)
- Tags: core | n_authors: 20
Hosts and their microbiomes coexist in a shared environment, engaging in dynamic interactions that are essential to maintaining health and modulating disease processes. To fully understand these interactions, spatially resolved and unbiased approaches are needed to map gene expression from both host and microbial cells within their native tissue context. Here, we present microDBiT, a spatial transcriptomic platform that enables simultaneous, high-resolution profiling of host and bacterial RNAs, including both mRNA and rRNA. Using microDBiT, we mapped the spatial distribution of host and microbial transcripts in the ileum and colon of germ-free mice, gnotobiotic mice colonized with a defined gut microbial community, and specific pathogen-free mice treated with dextran sulfate sodium (DSS) to induce colitis. We observed location-specific transcriptomic alterations in both host and bacterial cells in response to colonization and during inflammation. These results demonstrate the utility of microDBiT for dissecting host-microbiome interactions at high resolution and provide new insights into immune responses, spatial microbial localization, and microbiome-associated disease processes.

### PARG inhibition elicits cytotoxicity by sequestering XRCC1 and other PAR-binding proteins into PAR-dependent nuclear condensates.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78665-9
- First: Isaac Dumoulin | Last: Shan Zha (Institute for Cancer Genetics, Vagelos College of Physicians and Surgeons, Columbia University, New York City, NY, USA. sz2296@cumc.columbia.edu.; Department of Pathology and Cell Biology, Vagelos Col)
- Tags: secondary, disease | n_authors: 8
DNA breaks activate PARP1/2 to synthesize poly(ADP-ribose) (PAR), which relax chromatin and recruit DNA repair factors. PAR is normally short-lived and rapidly degraded by poly(ADP-ribose) glycohydrolase (PARG). While PARP1/2 inhibitors target homologous recombination (HR)-deficient cancers, predictive biomarkers for PARG inhibition (PARGi) remain undefined. Using genome-wide CRISPR screens, we find that PARGi is synthetically lethal with loss of multiple PAR-binding factors (XRCC1-LIG3/POLB, ALC1/CHD1L, ARH3, PARG itself) but not HR-deficiency. Conversely, loss of PARP1, NMNAT1 (nuclear NAD⁺ synthesis), or UNG confers resistance. Mechanistically, PARGi induces reversible PARP1- and PAR-dependent nuclear condensates in undamaged cells. While lacking detectable DNA breaks, these condensates sequester various PAR-binding proteins (e.g. XRCC1, ALC1, FUS), reducing their nuclear availability and impairing recruitment to bona fide DNA lesions. These findings identify PAR-binding protein sequestration as the mechanism underlying PARGi cytotoxicity, explain the paradoxical essentiality of PARG but not PARP1, and establish PAR-binding factor deficiency as a biomarker for PARGi.

### The Emirati pangenome featuring a diploid chromosome-level reference.
- Nature Communications | 2026-10-20 | https://doi.org/10.1038/s41467-026-78776-3
- First: Michael Olbrich | Last: Habiba Alsafar (Center for Biotechnology, Khalifa University of Science and Technology, Abu Dhabi, UAE. habiba.alsafar@ku.ac.ae.; Department of Biomedical Engineering and Biotechnology, Khalifa University of Science )
- Tags: core, secondary | n_authors: 19
Reference genomes are essential for identifying and representing human genomic variation, yet single-genome sequences fail to capture population-specific diversity. We present the Emirati pangenome comprising a trio-based, diploid chromosome-level assembly from deep, multi-platform sequencing data and 57 additional high-quality HiFi sequencing-based chromosome-scale assemblies, 27 of which are trio-based. Haplotypes demonstrate high contiguity (median N50 of 151.9 Mb) and good base accuracy (median QV score of 59.31). Of all assembled chromosomes, 31.8% are telomere-to-telomere (T2T) scaffolds (chromosome-spanning sequences flanked by telomeric repeats at both ends), and 64.3% achieved chromosome-level continuity (single scaffolds spanning an entire chromosome but retaining one or more sequence gaps or lacking a telomeric signature at one or both ends). These assemblies form the foundation of the population-specific pangenome graph of the Emirati Reference Genome Project (ERGP), which captures genomic variation comparable to the globally diverse HPRC reference graph, while covering regionally enriched variation. Applying the ERGP pangenome to short‑read genotyping of an independent...

### Optogenetic RNA relocalization reveals causal neural function in vivo
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.17.767469
- First: Cai, S. | Last: Qi, L. S.
- Corresponding: Lei S Qi (Stanford University)
- Tags: secondary | n_authors: 16
RNA localization dictates where translation occurs, yet its disease role is unclear because most assays manipulate abundance, not position. We develop an optogenetic CRISPR-dCas13 system (Opto-CRISPR-TO) that repositions endogenous RNAs with subcellular precision, second-scale kinetics, and reversibility, enabling causal tests in vivo. In cells, Opto-CRISPR-TO routes diverse RNAs to organelles and ribonucleoprotein granules with multiplex, bidirectional control, revealing distinct RNA behaviors in centrosomes and P-bodies. In mouse retina, acute (4-hour) mislocalization of Actb mRNA redirects {beta}-actin protein, remodels synaptic architecture and cell positioning, and persistently impairs vision. Thus, RNA location governs proteome topology and neural circuit output, and brief mislocalization drives lasting dysfunction. The approach generalizes across targets, compartments, and cell types, establishing a framework for probing RNA localization mechanisms in development, plasticity, and degeneration.

### HIPPO signaling competency links human stromal cell states to bone forming potential and osteogenic responsiveness
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.14.766622
- First: Caci, A. | Last: Rauch, A.
- Corresponding: Alexander Rauch (University of Southern Denmark)
- Tags: core | n_authors: 5
Skeletal stromal populations contribute to bone maintenance and repair, but how their molecular heterogeneity relates to bone forming potential remains incompletely understood. Whether shared transcriptional programs link this functional diversity to osteogenic responsiveness remains unresolved. We combined single-cell RNA sequencing of four human stromal clones with contrasting bone forming capacities, functional assays, and primary human stromal datasets. High bone forming clones shared oxidative metabolism and signaling-associated programs despite clone-specific expression patterns. Metabolic flux measurements supported these differences, whereas mixed implants provided no evidence of paracrine transfer of bone forming potential. We therefore examined signaling-associated competency states and identified a HIPPO competency signature enriched in high bone forming clones despite lower canonical YAP/TAZ target-gene expression. Unlike target-gene expression, competency-associated expression remained comparatively stable following pathway perturbation. Functionally, high bone forming clones showed greater osteogenic responses to both pharmacological activation and inhibition of YAP/T...

### How Much Can AI Virtual Cells Gain from Unified Perturbational Modeling?
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.10.25.761625 | version 2
- First: Wei, Z. | Last: You, Y.
- Corresponding: Yuning You (School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen (CUHK-Shenzhen))
- Tags: core | n_authors: 5
Predicting how individual cells respond to perturbations is a central task in artificial intelligence virtual cell (AIVC) modeling. However, integrating perturbation datasets is challenging because they differ in measured gene sets, perturbation types and cellular contexts. Existing AIVC predictors are typically developed for specific settings, limiting their applicability across heterogeneous datasets. Here, we investigate the extent to which AIVC predictors can benefit from unified perturbational modeling (UPM), a novel paradigm designed to integrate heterogeneous Perturb-seq datasets into a single predictive model. To this end, we introduce three unification modules into a variational autoencoder (VAE)-based AIVC predictor to address these sources of heterogeneity: gene-channel alignment, shared perturbation encoding, and joint embedding of gene expression and identity. We systematically evaluate and validate the individual contributions of these modules. Building on UPM, we assemble a dataset of 110 million cells spanning over 22,000 genes, four perturbation types and 76 cellular contexts, and use 89.7 million cells from 71 contexts to train a unified AIVC predictor with more t...

### CellVADIS: Inferring cross-tissue immune cell trafficking dynamics from single-cell snapshots
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.18.767220
- First: Wicker, L. | Last: Graw, F.
- Corresponding: Frederik Graw (FAU Erlangen-Nuernberg/ University Hospital Erlangen)
- Tags: core | n_authors: 4
The ability of immune cells to traffic between and enter different tissues is an important hallmark for effective immune responses. However, despite advances in high-throughput single-cell profiling, identifying circulating cell populations that drive tissue-specific immunity remains elusive. Here we present CellVADIS, an optimal transport based computational framework to infer cross-tissue immune cell dynamics. By connecting single-cell measurements across tissue sites, CellVADIS enables the prediction of cell migration fates, characterization of tissue-specific trafficking signatures on circulating cells, as well as identification of tissue entry points. We benchmarked our method against synthetic data and applied CellVADIS to two cross-tissue single-cell datasets which revealed characteristic marker expression patterns that define tissue-specific trafficking signatures and homing niches of tissue-entering CD4+ and CD8+ T cells. CellVADIS provides a flexible, open-source tool for identifying cross-tissue single-cell dynamics from various high-throughput single-cell measurements, which would support the design of vaccination and immunotherapeutic regimens to generate tissue-specif...

### Convergent Genomic Signatures of Selection in Thar: Genetic trade-offs for desert survival
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767204
- First: Rathod, S. M. | Last: Mukerji, M.
- Corresponding: Mitali Mukerji (Indian Institute of Technology, Jodhpur)
- Tags: secondary | n_authors: 3
Background: Desert environments provide a setting for natural biological experiments to cope up with simultaneous stressors of extreme temperatures, aridity, UV exposure, and limited food resources. Biological adaptations that support living in such an environment could become liabilities when the environment and lifestyle change due to gene-environment mismatch. We explored whether genetically and culturally diverse endogamous native populations of the Thar exhibit convergent signatures of selection to desert conditions and whether the selected loci have implications in traits and disease susceptibilities relevant to non-native transitions. Results: We report 348 high-confidence variants across 45 candidate genes from a study on 176 individuals from eight genetically distinct Thar populations. These genes identified from humans and other desert inhabitants display convergent evolution with multiple selection scans (PBSn1, Tajima`s D, iHS, and XPEHH) in diverse Thar populations. Prominent genes include ZNF385D, SGCZ, SARDH, SLC12A3, etc. Selected variants essential in the desert environment were associated with complex traits like lipid metabolism, hypertension, renal and cardiovas...

### Targeting AURKA by CRISPR/SaCas9 Alters Cell Cycle Progression and Enhances Lenvatinib-Associated Reduction in Cell Viability in Hepatocellular Carcinoma: An Integrated In Silico and HepG2 in Vitro Study
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.17.767223
- First: Taibe, N. S. | Last: Mohamed, R. H.
- Corresponding: Rania Hassan Mohamed (Ain Shams University)
- Tags: secondary, disease | n_authors: 5
Hepatocellular carcinoma (HCC) presents substantial clinical concerns as a result of its high treatment resistance, frequent recurrence, and strong correlation with chronic liver diseases. Aurora kinase A (AURKA) is overexpressed in HCC correlating with poor prognosis and treatment resistance. Our bioinformatics analyses revealed that AURKA overexpression in HCC is associated with mitotic proteins and oncogenes, emphasizing its role in cancer progression. CRISPR/SaCas9-mediated AURKA knockdown markedly reduced AURKA expression levels through inducing several indels in the AURKA gene sequence, resulting in functional consequences including upregulation of p21, p53, and caspase-8, as well as downregulation of CDK1, CDK2, PI3K (alpha subunit), P38, and BCL-2 genes. Flow cytometry verified that these alterations were compatible with G2-phase cell cycle arrest and slight activation of apoptosis. Also, scratch and colony formation assays indicated a significant reduction in metastatic and proliferative potential. Furthermore, AURKA knockdown combined with Lenvatinib significantly reduce HepG2 cell viability compared with either treatment alone. Mechanistically, this study indicated that ...

### TRAIT: A Toolbox for Rapid Assembly of Integration Templates for CRISPR/Cas- and Integrase-Mediated Genome Engineering
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767390
- First: Timofeev, O. | Last: Schacht, P.
- Corresponding: Oleg Timofeev (Philipps University of Marburg)
- Tags: secondary | n_authors: 4
The generation of genetically engineered mammalian cell models often requires repeated construction of integration donors that differ in their targeting sequences, genetic payloads, or integration strategies. Although modular DNA assembly methods facilitate construct generation, adapting existing expression cassettes to different genome-engineering applications remains labor-intensive. Here, we present TRAIT (Toolbox for Rapid Assembly of Integration Templates), a modular cloning framework that combines direct Golden Gate assembly of targeting elements with Gateway-mediated transfer of genetic payloads. The core vector architecture separates genome-targeting sequences from payload assembly, allowing existing Gateway-compatible constructs to be reused without modification of internal Type IIS restriction sites. We developed vector modules supporting homology-directed repair, homology-independent targeted integration, FrameSelect-compatible donor cleavage, coordinated guide RNA delivery, inducible Cas9 expression, Bxb1-mediated cassette exchange, and conditional transgene expression. An extended MultiSite Gateway workflow enables the assembly of complex integration donors using indep...

### Tracking the trajectory of individual conjugative plasmids in bacterial communities using CRISPR acquisition-based recording
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767295
- First: Fernandez-Gomez, A. | Last: Llosa, M.
- Corresponding: Matxalen Llosa (Instituto de Biomedicina y Biotecnologia de Cantabria - Universidad de Cantabria)
- Tags: secondary | n_authors: 9
Horizontal gene transfer mediated by conjugative plasmids is a primary driver of bacterial evolution and the spread of adaptive traits, including antibiotic resistance determinants. Tracking how these plasmids disseminate through complex microbial communities remains a major challenge. Current methodologies often yield static, endpoint snapshots of host identity, overlooking transient transfer events and plasmid encounters with the co-resident mobilome. To overcome these limitations, we introduce SPacer Integration (SPI) plasmids, which turn the mobile element itself into a recorder of its own transfer history. We engineered conjugative and mobilizable plasmids to carry a CRISPR-Cas adaptation cassette (cas1-cas2 and a minimal CRISPR array) and maintain tight repression of cas1-cas2 expression in the donor cell, so that upon transfer they capture spacers from the chromosome and plasmids of new hosts and store them permanently in their own array. Subsequent PCR amplification and sequencing of these expanded arrays provide a molecular record of both the bacterial hosts and the co-resident plasmids encountered. We created SPI plasmids using the backbones of well-characterized mobiliza...

### Breastfeeding Enables Systemic Transfer of Functional Maternal Immune Cells to Neonates
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767284
- First: Naftaly, S. | Last: Zinger, A.
- Corresponding: Assaf Zinger (Technion)
- Tags: core | n_authors: 9
Does breastfeeding transfer living maternal immune cells that persist and function in offspring, beyond providing soluble immune factors? Using a foster-nursing mouse model that eliminates prenatal exposure, this study directly tests whether maternal cells can be transferred postnatally through breastmilk. We found that intact maternal immune cells survive neonatal gastrointestinal transit, enter the circulation, and disseminate to peripheral organs. Single-cell RNA sequencing shows that transferred cells span multiple hematopoietic lineages, dominated by monocyte-derived macrophages with a distinct stress-adapted, inflammatory transcriptional state compatible with persistence in the neonatal environment. Interestingly, these maternal cells are detected at sites of neonatal tissue injury, consistent with chemotactic responsiveness. Our findings suggest that breastfeeding may serve as a postnatal route for maternal cellular transfer, potentially extending maternal immune influence beyond gestation.

### VPHYL: A Web Application for Converting Emu and EPI2ME wf-16s Nanopore 16S rRNA Abundance Tables into phyloseq and BIOM Objects
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767361
- First: Ramireddy, V. S. R. | Last: Srivastava, S. K.
- Corresponding: Sarvesh Kumar Srivastava (Indian Institute of Technology (IIT), Delhi)
- Tags: core | n_authors: 2
Taxonomic abundance data derived from 16S rRNA gene sequencing data are fundamental in microbiome research. To perform downstream statistical analysis and visualization, raw abundance data must typically be converted into standardized data structures, such as phyloseq S4 objects or BIOM files. This conversion requires three input data files: an Operational Taxonomic Unit (OTU) table (count of specific taxa across samples), a Taxonomy table (hierarchical lineage from Kingdom to Species), and a Sample Data table (experimental metadata). For Oxford Nanopore (ONT) 16S data, the two commonly used classifiers, Emu and the EPI2ME wf-16s workflow (Minimap2/Kraken2), generate output files with different formats and column schemas. We found no web-based tool that accepts these classifier outputs directly. Experienced users can reshape them with a script. Researchers who do not program cannot, and for them, this step remains a hurdle. We introduce VPHYL(Versatile PHYLogenetic Standardizer), an R Shiny web application that accepts abundance outputs directly from Emu and EPI2ME wf-16s, splits the lineage into standard ranks, attaches sample metadata, and generates phyloseq objects or BIOM files...

### The KMT2A-MENIN complex is a therapeutic vulnerability in SETBP1-mutant leukemia
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.765711
- First: Tauchmann, S. | Last: Maxson, J. E.
- Corresponding: Julia E Maxson (Oregon Health and Science University)
- Tags: secondary, disease | n_authors: 6
SET binding protein 1 (SETBP1) is recurrently mutated in high-risk myeloid malignancies, including myelodysplastic/myeloproliferative overlap disorders (MDS/MPNs) and is associated with poor clinical outcomes. Although SETBP1 mutations promote self-renewal and HOX-driven transcription in murine and cell line models, the epigenetic dependencies sustaining these programs in human hematopoietic stem and progenitor cells (HSPCs) remain poorly defined. Here, we identify the KMT2A-MENIN complex as a targetable dependency in SETBP1-mutant leukemia. Expression of SETBP1D886N enhanced growth and serial replating of human HSPCs and established a transcriptionally permissive chromatin state, with increased H3K4me3, H3K27ac and KMT2A occupancy at SETBP1-regulated loci. Integrated transcriptional and chromatin profiling defined a 94-gene SETBP1 regulome containing HOXA9, MEIS1, MECOM, and MYBand was enriched for transcriptional programs associated with KMT2A-rearranged, NUP98-HOXA9, and NPM1-mutant leukemias. CRISPR-Cas9 disruption revealed a functional requirement for KMT2A, but not for KMT2B or DOT1L in SETBP1D886N HSPCs. Strikingly, deletion of the KMT2A cofactor MEN1 phenocopied KMT2A loss....

### Immune Age Acceleration Stratifies Survival in Multiple Myeloma Independent of Chronological Age and Clinical Fitness
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767344
- First: Ferguson, K. E. | Last: Bhasin, M.
- Corresponding: Manoj Bhasin (Emory University)
- Tags: core | n_authors: 28
Chronological age incompletely explains prognostic heterogeneity in multiple myeloma (MM), particularly among younger patients, whose clinical outcomes vary widely. Existing immune aging clocks are predominantly derived from peripheral blood expression data and thus incompletely reflect the aging of the bone marrow (BM) immune microenvironment in MM. To address this limitation, we developed BM immune aging clocks for ten immune and progenitor cell types trained on single-cell RNA-sequencing data from 1,260 healthy peripheral blood and BM samples and calibrated to BM. We then applied these clocks to BM single-cell profiles from 337 newly diagnosed MM patients enrolled in the CoMMpass study to derive a global immune age acceleration score. In patients younger than 70 at diagnosis, accelerated immune aging was independently associated with shorter overall survival (OS; HR = 2.24, p = 0.003) after adjustment for cytogenetic risk, transplant status, triplet therapy administration, chronological age, sex, performance status, and laboratory deficits, whereas chronological age was not predictive. Subsequent analyses identified CD4+ memory T cell aging as the strongest contributor to overal...

### Subtype-specific autophagy profiles in Renal Cell Carcinoma
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767069
- First: Kasikci, F. | Last: Knaevelsrud, H.
- Corresponding: Helene Knævelsrud (Department of Molecular Medicine, Institute of Basic Medical Sciences, University of Oslo, Oslo, Norway; Centre for Cancer Cell Reprogramming, Institute of Clin)
- Tags: secondary, disease | n_authors: 14
Autophagy is a highly conserved cellular mechanism essential for recycling intracellular components and providing energy and maintaining cellular homeostasis. The role of autophagy in cancer is double sided, where it can suppress tumorigenesis by degrading damaged organelles and preventing chronic inflammation while supporting survival of existing tumor cells to survive during starvation and stress, and thus support tumor growth. The role of autophagy in renal cell carcinoma (RCC), the most common type of kidney cancer, remains insufficiently described. RCC originates from epithelial cells of the renal tubule and is divided into histological subtypes where clear cell RCC is the most common followed by papillary and chromophobe RCC, showing differences in morphology and molecular features. Recent studies of RCC suggest that mTORC1 and autophagy are involved in kidney cancer development and response to treatment, advocating the need to better understand the role of autophagy in RCC. To this end, we investigated autophagy markers by immunostaining, immunoblotting and quantitative PCR in biobanked fresh-frozen tissue samples of RCC tumor and matched normal tissue. Overall, we found red...

### Cerulean Protein Tagging Enhances Immunogenicity and Osimertinib Response of Transplantable Murine EGFR Mutant Lung Cancer Cell Lines
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767321
- First: Avila, J. T. | Last: Heasley, L. E.
- Corresponding: Lynn E Heasley (University of Colorado Anschutz Medical Campus)
- Tags: secondary, disease | n_authors: 6
Lung cancers bearing mutations in epidermal growth factor receptors (EGFR) exhibit marked, but incomplete responses to tyrosine kinase inhibitors (TKIs) like osimertinib. We previously developed genetically-engineered mouse models (GEMMs) for EGFR exon 19 deletion (del19) and L860R (mouse equivalent of L858R). Sequences encoding mC3 cerulean fluorescent protein were included to mark emergent tumor cells. Orthotopic implantation of mEGFRdel19 cell lines into syngeneic C57BL/6J mice yielded tumors that were eliminated upon osimertinib therapy which is not typically observed in patients while mEGFR-L860R cell lines failed to establish tumors. Herein, mEGFRdel19 and mEGFR-L860R cell lines formed tumors in non-induced mEGFRdel19 and mEGFR-L860R GEMMs and green fluorescent protein-transgenic mice, supporting mC3-derived epitopes as mediators of immunoelimination. CRISPR-Cas9 mediated disruption of the mC3 cerulean sequence in established mEGFR cell lines yielded two independent mC3-deleted cell lines that formed orthotopic tumors and exhibited partial osimertinib responses. These studies provide a cautionary tale regarding use of fluorescent proteins in murine cancer models and reinforce...

### The Neuroimmune Signature Underlying HPV Infection and Cervical Cancer Progression
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.766177
- First: Correa, Y. L. G. | Last: Cabral-Marques, O.
- Corresponding: Yohan Lucas Goncalves Correa (Department of Clinical and Toxicological Analyses, School of Pharmaceutical Sciences, University of Sao Paulo (USP), Sao Paulo, Brazil)
- Tags: core, disease | n_authors: 17
Persistent infection with high-risk human papillomavirus (HPV) is the principal cause of cervical cancer, yet the multicellular signalling programmes that accompany disease progression remain incompletely defined. Here, we integrated Single cell RNA sequencing, independent microarray and bulk RNA-sequencing meta analyses, and TCGA CESC tumor data to characterize the neuroimmune transcriptional architecture of HPV associated cervical disease. Single cell profiling revealed progressive remodeling of epithelial, stromal, endothelial and immune compartments across HPV infection, high grade squamous intraepithelial lesions and cervical cancer. Although immune dysregulation predominated, lesion and tumor states showed coordinated enrichment of nervous system associated programs, including synapse organization, trans-synaptic signaling, axon development, neurogenesis and neurotransmitter-related signaling. These programs formed interconnected networks with cytokine production, leukocyte activation, chemotaxis, cell adhesion, apoptosis, and immune effector regulation. Cross-platform integration identified a recurrent 12-gene neuroimmune signature associated with tumor grade related transcr...

### RapidGLM: genome-scale differential expression, CRISPR screen and eQTL analysis
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767389
- First: Hung, L.-H. | Last: Yeung, K. Y.
- Corresponding: Ling-Hong Hung (University of Washington Tacoma)
- Tags: secondary | n_authors: 2
Genome-scale differential expression, CRISPR screen and expression QTL analyses fit millions of count regressions and estimate p-values from billions of random draws. RapidGLM, a C++ library, makes both steps fast, with Newton fits specialized to count models and draws made in batches. Its DESeq2, edgeR, SCEPTRE and cis-QTL analyses agree with the reference tools and run 2.5-17.8 times faster on the same cores. On one compute node, a CRISPR screen's 28.0 million tests took SCEPTRE 11.6 hours and RapidGLM 44 minutes, or 2.8 hours with more accurate small p-values. RapidGLM is MIT-licensed, with C, Python, R and command-line interfaces.

### Agentic Discovery Transfer Enables Cross-Cancer Discovery at Scale
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.10.28.762506 | version 3
- First: Cheng, L. | Last: Kendziorski, C.
- Corresponding: Christina Kendziorski (University of Wisconsin)
- Tags: core, disease | n_authors: 9
Cancer research generates tens of thousands of studies each year, yet whether a published finding holds in another cancer type or patient population is rarely tested as doing so is labor-intensive and difficult to scale. We define this task as discovery transfer and present SMART, a multi-agent large language model framework for discovery transfer in single-cell RNA-sequencing studies. Given a source manuscript and a target dataset, SMART extracts major clinical and mechanistic findings, generates and executes analyses for the testable findings, reports which findings transfer, and suggests follow-up. Applied to 121 studies across six cancer types, SMART identified findings that transfer across cancers, including a lung cancer prognostic signature that we confirmed to be associated with survival in liver cancer, pancreatic cancer and pleural mesothelioma. SMART also generated new mechanistic hypotheses, demonstrating how agentic discovery transfer can extend published findings beyond their original setting.

### LRCQ: phenome-wide heritability enrichment of genomic loci from GWAS summary statistics
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.02.763731 | version 2
- First: Chen, L. G. | Last: Sham, P. C.
- Corresponding: Lane Guolan Chen (The University of Hong Kong)
- Tags: secondary | n_authors: 3
Some genetic variants are associated with many traits, but a variant's GWAS statistics are also inflated by the effects of variants in LD with it and by confounding shared by all variants in a study. Existing measures of per-variant pleiotropy, such as counts of significant associations or multi-trait association tests, do not separate these sources. Stratified LD score regression separates them for one trait at a time and only through predefined annotations. We present LRCQ (LD score regression on {chi}2 across many GWAS), which estimates for each locus its phenome-wide heritability enrichment: the variance of its causal effects across a set of traits, relative to an average locus. LRCQ regresses squared Z-scores from 30 or more GWAS jointly on squared LD, with per-trait LDSC intercepts and heritabilities fitted in earlier stages. Its pooled least-squares solution has a closed form whose cost does not grow with the number of traits. Its standard errors account for sample overlap and genetic correlation between GWAS. Squared Z-scores identify enrichment at the resolution of LD clumps, not single SNPs, so LRCQ reports clump-level estimates ("omni-loci"). These estimates can be aggre...

### LRCP: identifying functionally related SNPs and genes from phenome-wide genetic-effect correlations using GWAS summary statistics
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.02.763742 | version 2
- First: Chen, L. G. | Last: Sham, P. C.
- Corresponding: Lane Guolan Chen (The University of Hong Kong)
- Tags: secondary | n_authors: 3
Genetic correlation describes which traits share genetic causes. The transposed question, which variants act alike across the phenome, has no comparable estimator, although it points directly to shared genes, pathways and regulators. Correlations of GWAS Z scores between variants across many traits are easy to compute, but they are confounded by linkage disequilibrium (LD) and, for any pair of variants, by sample overlap and genetic correlation among the GWAS. We show that in 452 Pan-UK Biobank GWAS the effective number of independent traits is only 58, and that naive tests reject 51-70% of null pairs of distal variants. We introduce LRCP (likelihood and regression on cross-products of Z scores), which estimates the phenome-wide genetic-effect correlation{rho} between SNPs by regressing Z-score cross-products on LD cross components, using per-SNP heritability enrichment from the companion method LRCQ and LDSC-derived plug-ins. For variants in different LD blocks the estimator has a closed form, and its standard errors account exactly for the dependence among GWAS. In simulations LRCP is unbiased (absolute bias at most 0.03), its 95% intervals cover 93-98%, and its type-I error is 5...

### Zhx2 expression in the mouse brain
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.11.765907
- First: Miracle, S. | Last: Bryant, C. D.
- Corresponding: Camron D. Bryant (Laboratory of Addiction Genetics, Department of Pharmaceutical and Biomedical Sciences and Center for Drug Discovery, Northeastern University, Boston, MA USA)
- Tags: secondary | n_authors: 9
Prescription opioids like oxycodone (OXY; the active component in OxyContin) continue to drive the ongoing opioid use disorder (OUD) epidemic due to their widespread prescription and distribution. Genetic factors influencing pharmacokinetic and pharmacodynamic properties of opioids can have profound impacts on drug response and, in turn, influence risk for OUD. We previously used quantitative trait locus (QTL) mapping and gene validation to identify zinc-finger homeobox 2 (Zhx2) loss-of-function as a quantitative trait gene and mechanism underlying increased brain concentration of oxymorphone (OMOR) following systemic administration of OXY in BALB/cJ females that was linked to increased OXY reward. To test whether we could rescue the behavioral phenotype, we overexpressed Zhx2 in the brain via retro-orbital injection of a brain-specific adeno-associated virus (AAV). We observed restricted Zhx2 expression (especially females), with more widespread expression in males. Consequently, we did not observe any significant effect of brain Zhx2 overexpression on OXY reward as measured via conditioned place preference (CPP). However, Zhx2 overexpression did protect against OXY-induced weight...

### Spatial and epigenetic programs underlie heterogeneous cellular senescence in the aging liver
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767706
- First: Mamde, S. | Last: Zemke, N. R.
- Corresponding: Nathan R. Zemke (Department of Cellular and Molecular Medicine, University of California, San Diego School of Medicine, La Jolla, CA, USA; Center for Epigenomics, University of )
- Tags: core | n_authors: 43
Aging is a complex biological process leading to tissue dysfunction, and driven in part by progressive epigenetic drift, widespread transcriptional dysregulation and cellular senescence. Senescent cells (SnCs) accumulate across tissues in a heterogeneous and cell type-specific manner, yet their molecular signatures and spatial organization within native tissue have not been systematically mapped. Here we combined single-nucleus transcriptomic, epigenomic, three-dimensional (3D) genome and spatial profiling to systematically characterize aging of the mouse liver and associated cellular senescence. Aging was marked by hepatocyte loss, immune cell expansion, erosion of repressive H3K9me3 heterochromatin, alteration of 3D genome organization, and activation of stress-response pathways known to promote senescence. Age-associated SnCs were spatially colocalized within discrete inflammatory microenvironments termed SenSpots. Different SenSpots were dominated by distinct hepatocyte senescence states (senotypes), driven by unique transcription factors, and exhibited distinct lobular zonation. Single-cell DNA methylation profiling revealed a subset of immune cells in aged livers with loss of...

### A single-cell transcriptomic atlas of T cells across murine lymphoid, mucosal, and gland tissues
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767759
- First: Wang, X. | Last: Zhao, X.
- Corresponding: Xiang Zhao (Center for Excellence in Molecular Cell Science)
- Tags: core | n_authors: 7
T cells play essential roles in immune surveillance, host defense, and tissue homeostasis, with their cellular composition and transcriptional states varying across tissues. In this study, we constructed an integrated single-cell transcriptional atlas of 124,186 T cells from seven organs of healthy mice. We identified shared T cell states with distinct tissue associated distributions and transcriptional features. Further analyses revealed transcriptional changes associated with thymocyte maturation, diverse innate-like and memory-like T cell populations in bone marrow, and distinct regional distributions of CD8-like T cell states in the intestine. The submandibular gland contained diverse naive, helper-associated, and effector-associated T cell states. pySCENIC analysis further revealed tissue associated variation in inferred transcription factor regulon activity within shared T cell populations. Together, these findings provide a single cell reference for understanding T cell heterogeneity across lymphoid and non-lymphoid tissues under physiological conditions.

### BPEA integrates pleiotropy and epistasis to guide allele pyramiding for multi-trait crop improvement
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.19.767812
- First: Li, X. | Last: Lu, K.
- Corresponding: Kun Lu (Southwest University)
- Tags: secondary | n_authors: 8
Dissecting the genetic basis of complex traits and pyramiding favorable alleles are central to crop breeding. However, jointly evaluating pleiotropy and epistasis to identify allele combinations that meet multiple breeding objectives remains challenging. Here, we present BPEA (Bayesian Pleiotropy and Epistasis Analysis), a Bayesian framework integrating LD-guided QTL interval identification, joint genetic inference and allele-combination assessment. BPEA uses the joint posterior to estimate the posterior probability of simultaneous improvement (PPSI) between allele combinations and ranks them by mean PPSI. In simulations, BPEA improved interval identification and epistatic interaction attribution relative to comparator methods and maintained high precision in shared-signal detection. When epistasis was present, it reduced mean combination-selection regret by 68.4-86.3% relative to a model without interaction terms. Applications to three rapeseed populations identified shared genetic signals and candidate epistatic interactions associated with seed-quality traits. BPEA also prioritized allele combinations for simultaneous reductions in erucic acid and glucosinolate contents and iden...

### Causal regulators of human T-cell and macrophage activation from perturbation screens, and a replicated coupling of T-cell exhaustion markers with macrophage M1 activation in patients under checkpoint blockade
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767605
- First: Cupaioli, F. A. | Last: Merelli, I.
- Corresponding: Ivan Merelli (CNR-ITB)
- Tags: core, secondary, disease | n_authors: 2
Engineering anti-tumour immunity requires knowing which genes control T-cell and macrophage programs, and how the two compartments relate to each other in patients. We built ImmunoTwin, an analysis framework that addresses both questions with public data and with every test, baseline and criterion fixed before the result was computed. From a genome-scale CRISPR-interference Perturb-seq in primary human CD4+ T cells (22 million cells, four donors) we derive a map of regulators of the cytotoxic effector program that is calibrated, reverses direction under CRISPR activation (rho = -0.53), and tracks interferon-gamma production among the hits of independent sorting-based screens (rho = 0.69). From a Perturb-seq in primary human macrophages we recover the TLR4-NF-kappaB pathway as regulator of the lipopolysaccharide response (pathway-level P = 0.0004) and find that transcriptional effects track TNF protein measured in independent donors (rho = 0.58). In both cell types, however, a generic measure of perturbation strength recovers the hits of functional screens better than the program-specific effect (area under the ROC curve 0.96 versus 0.73 in T cells; 0.87 versus 0.72 in macrophages)....

### PDAC BioPortal: An Integrated Web Resource for Multi-Scale Analysis of Pancreatic Cancer Transcriptomics
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767683
- First: Kumar, P. | Last: Vlashi, E.
- Corresponding: Prince Kumar (University of California Los Angeles)
- Tags: core, disease | n_authors: 2
Pancreatic ductal adenocarcinoma (PDAC) exhibits extensive molecular heterogeneity and undergoes substantial transcriptional remodeling across disease and treatment contexts. However, publicly available PDAC transcriptomic resources remain fragmented across experimental modalities, limiting the integrated investigation of molecular programs across biological scales and cellular compartments. Here, we developed PDAC BioPortal, an integrated web-based analytical resource for multimodal interrogation of PDAC transcriptomics. The platform incorporates bulk RNA sequencing, treatment-associated transcriptomics, single-nucleus RNA sequencing, and spatial transcriptomics. It integrates 349 TCGA-GTEx samples, including a primary tumor-versus-normal comparison of 178 PDAC tumors and 167 normal pancreas specimens; a clinically annotated treatment-associated cohort of 55 specimens (GSE225767); a single-nucleus atlas comprising 224,988 nuclei from 43 patients (GSE202051); and spatial transcriptomic profiles encompassing 23,436 tissue spots from five patients (GSE274103). The platform provides interactive differential expression analysis, over-representation analysis, gene set enrichment analysi...

### Site-Specific and Diet-Dependent Genetic Architecture of Trabecular Bone in Male BXD Recombinant Inbred Mice
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767695
- First: Chanpaisaeng, K. | Last: Fleet, J. C.
- Corresponding: James C Fleet (University of Texas at Austin)
- Tags: secondary | n_authors: 5
Vertebral fracture risk is influenced by trabecular bone (Tb) microarchitecture, a phenotype that is regulated by genetic and environmental factors. We examined the genetic architecture of Tb microarchitecture in the fifth lumbar vertebra (L5) and its modification by dietary calcium (Ca). Male mice from 51 BXD recombinant inbred lines were fed adequate (0.5%) or low (0.25%) Ca diets from 4 to 12 weeks of age. Micro-computed tomography (CT) was used to assess seven L5 Tb phenotypes, and the response to Ca restriction (RCR) was calculated for each phenotype. Quantitative trait loci (QTL) were identified by composite interval mapping and compared with previously reported femoral Tb QTL from the same mice. Genetic background significantly influenced all L5 phenotypes and their responses to Ca restriction. We identified 127 QTL distributed across 61 loci. First, very few L5 QTL overlapped those previously identified in the femur, providing strong evidence for skeletal site-specific genetic regulation of Tb microarchitecture. Second, QTL detection was strongly dependent on dietary Ca, with only 4 of 33 loci identified under adequate Ca intake also detected under low Ca intake. Third, QTL...

### Cell-type-resolved methylation analysis using bulk long-read sequencing across human tissues
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767445
- First: Chen, H. | Last: Fang, G.
- Corresponding: Gang Fang (Icahn School of Medicine at Mount Sinai)
- Tags: core, disease | n_authors: 31
DNA methylation shapes cellular identity and changes with aging and disease, but most human methylomes come from bulk tissue, which mixes signal across many cell types. A methylation change at the bulk tissue level can reflect a change in cellular composition or an intrinsic shift within a cell type, and the two cannot be separated from bulk data. Single-cell and sorted-cell methods resolve cell types directly, but their cost and workflow complexity pose challenges to large studies. Long-read sequencing of single DNA molecules can directly detect DNA methylation on each read. We built COMET (Cell-of-Origin from METhylation), a framework that uses cell-type-specific methylation to assign individual long reads to cell types from standard bulk long-read sequencing. COMET detects changes in cell-type composition robustly even from shallow bulk long-read data, quantifies methylation level of repetitive DNA within each cell type, and, with deeper sequencing, resolves methylation differences between health and disease in individual cell types. We applied COMET to 140 human blood samples, 104 human brain samples and 59 human colon samples. In blood, we found epigenetic aging clock is prima...

### Haplotype reconstruction in multi-generational diploid and tetraploid populations
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767397
- First: Zheng, C. | Last: Endelman, J. B.
- Corresponding: Jeffrey B. Endelman (University of Wisconsin-Madison)
- Tags: secondary | n_authors: 4
Previously, we developed a statistical framework and software (PolyOrigin1) to reconstruct parental haplotypes of each offspring in connected tetraploid F1 populations. A key application of the technology is quantitative trait loci (QTL) mapping, via regression of phenotypes on posterior probabilities of parental origins. In this work, we extend the methodology and software (PolyOrigin2) to multi-generational populations (both diploid and tetraploid), which are common in breeding programs. The extension links parental origins across generations to estimate posterior probabilities of founder origins. Compared to PolyOrigin1, the main challenge is to phase intermediate individuals that are both parents and offspring, which is overcome by the Bayesian update rule. In addition, genotypic error models are extended to account for sequencing errors such as allelic bias and overdispersion in genotyping-by-sequencing (GBS). Extensive simulations were used to compare PolyOrigin2 with previous methods and to study the effects of such variables as sequencing errors and the number of progeny per parent. We further evaluated PolyOrigin2 using three real datasets: diploid potato with 23 founders ...

### Single-cell analysis identifies concurrent type 2 and interferon programs in experimental eosinophilic esophagitis
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767761
- First: Dsilva, A. | Last: Munitz, A.
- Corresponding: Ariel Munitz (Tel Aviv University)
- Tags: core | n_authors: 10
Background & Aims: Eosinophilic esophagitis (EoE) is a chronic, type 2 cytokine-driven allergic disease of the esophagus. How the immune and structural cell landscape of the esophagus changes between healthy and inflamed tissue requires further investigation. Methods: CD45-enriched esophageal cells from naive and oxazolone (OXA)-challenged wild-type mice were profiled by single-cell RNA sequencing. A cytokine-gated gene expression score identified type 2 program-high cells. Findings were compared with published human esophageal datasets, validated histologically, and examined in Il13ra1-/- mice. Results: A total of 62,245 esophageal cells were analyzed. ILC2s accounted for most type 2 cytokine-expressing lymphocytes in naive mice, whereas Th2 cells accounted for approximately 80% following OXA challenge. ILC2s concurrently lost Il5, Il13 and Gata3 expression while retaining Areg. Resident memory-like CD8 T cells became the largest lymphoid population. Mast cells switched from a connective tissue-type to a mucosal-type and partly cycling state, which was confirmed by increased MCPT1 cells. Esophageal eosinophils displayed a signature resembling skin eosinophils of atopic dermatitis ...

### Continuous karyotypic and cryptic structural fluctuations drive acral melanoma evolution
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767656
- First: Smith, E. A. | Last: Judson-Torres, R. L.
- Corresponding: Robert L Judson-Torres (Huntsman Cancer Institute)
- Tags: core, disease | n_authors: 12
Reliable chromosome segregation during mitosis is essential for high-fidelity mammalian cell division. Even human cancers burdened by whole genome duplication and aneuploidy generally retain sufficiently stable segregation to produce clonal populations of progeny. Cancer genomes are accordingly understood to evolve in punctuated bursts, in which catastrophic rearrangement is followed by clonal expansion of a stabilized karyotype. However, bulk genomic sequencing, the workhorse of cancer genetics for the past two decades, cannot resolve structural variability within tumor subpopulations. Here we identify a subset of cancers that exhibit continuous ultra-low fidelity chromosomal segregation, with single tumors harboring individual cells whose metaphase chromosome counts ranged from 25 to over 200. This remarkable phenotype is recurrent in multiple cancer types and most common in acral melanoma, where it is associated with dicentric chromosomes, translocations, and complex structural variants. Single-cell whole genome sequencing revealed ongoing structural variation and the genomic signature of microhomology-mediated break-induced replication (MMBIR), a backup DNA repair pathway that ...

### A new liability-based rare-variant burden test identifies a novel genetic association between HTRA3 and idiopathic pulmonary fibrosis
- medrxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.26368326
- First: Chun, S. | Last: Raby, B. A.
- Corresponding: Sung Chun (Boston Children's Hospital)
- Tags: secondary | n_authors: 12
In contrast to large-effect monogenic variants, which are highly penetrant regardless of genetic background, variants with more modest effect sizes depend on a carrier's genetic background to manifest disease. For many complex traits, including idiopathic pulmonary fibrosis (IPF), polygenic risk scores (PRS) have been shown to capture a significant proportion of the genetic background risk. While a rare-variant association test incorporating a PRS covariate to account for the genetic background has been demonstrated to improve statistical power for gene discovery in quantitative traits, for binary traits, this approach shows limited or no power gain over PRS-unadjusted tests. Here, we propose a novel rare-variant association test for binary traits that jointly models the contribution of rare variants and PRS under a liability threshold model. In simulated datasets, our new method, liability threshold burden test (LTBT), shows a well-controlled false positive rate and outperforms the sensitivity of existing methods. To demonstrate this new method, we apply it to sequencing datasets for IPF, a rare but highly morbid lung disease. By accounting for an individual's genetic background w...

## Keyword hits: disease only (32)

### What do various cancers have in common?
- Nature | 2026-11-19 | https://doi.org/10.1038/d41586-026-03379-3
- First: Joanna Maria Kalucka | Last: Joanna Maria Kalucka
- Tags: disease | n_authors: 1
(no abstract in metadata)

### Balancing redox-mediated cytotoxicity and catalysis in natural product biosynthesis
- Science | 2026-11-19 | https://doi.org/10.1126/science.aee2641
- First: Hannah A. Boesger | Last: David H. Sherman (Life Sciences Institute, University of Michigan, Ann Arbor, MI, USA.; Department of Medicinal Chemistry, University of Michigan, Ann Arbor, MI, USA.; Department of Chemistry, University of Michigan, A)
- Tags: disease | n_authors: 11
Redox-mediated chemistry is central to both the biosynthesis and cytotoxicity of many natural products, yet how microbes balance these processes remains poorly understood. Here, we uncover a conserved mechanism that coordinates three redox-mediated processes in secondary metabolite biosynthesis: self-protection, prevention of substrate degradation, and late-stage biosynthesis. Using the antitumor antibiotic doxorubicin as a model system, we show that the vicinal oxygen chelate (VOC) protein DnrV...

### Characterizing the solution space of migration histories of metastatic cancers with MACH2
- Nature Methods | 2026-11-19 | https://doi.org/10.1038/s41592-026-03321-5
- First: Mrinmoy S. Roddur | Last: Mohammed El-Kebir
- Tags: disease | n_authors: 8
Abstract Metastases arise when cancer cells disseminate from the primary tumor, or other metastases, and seed tumors at distant anatomical sites. Reconstructing migration histories from DNA sequencing data is key to understanding the cellular mechanisms underlying metastatic dissemination. While the data often support many equally plausible histories, current methods return a single solution or sample alternatives without guarantees of optimality or completeness. Here we introduce MACH2, which e...

### In vivo programming of dual-targeted CAR-T cells facilitates vascular disruption and T-cell infiltration in solid tumors
- Nature Communications | 2026-11-19 | https://doi.org/10.1038/s41467-026-79342-7
- First: Mengyao Li | Last: Suping Li
- Tags: disease | n_authors: 17
(no abstract in metadata)

### Mitigating brittleness in ceramics via transformation- and twinning-induced plasticity
- Nature Communications | 2026-11-19 | https://doi.org/10.1038/s41467-026-79377-w
- First: Yong Huang | Last: Zaoli Zhang
- Tags: disease | n_authors: 9
Abstract Ceramics usually exhibit inherent brittleness at room temperature due to their strong covalent/ionic bonding and few active slip systems. Consequently, ceramics exhibit a low damage-bearing capacity and typically sudden failure prior to yielding. Thus, achieving room-temperature plasticity while maintaining or enhancing the strength of ceramics remains critical and challenging. Here, we report a promising strategy to address this problem by concurrently activating twinning-induced plast...

### Genomic mediators of acquired resistance to immunotherapy in metastatic melanoma
- Cancer Cell | 2026-11 | https://doi.org/10.1016/j.ccell.2026.10.011
- First: Julia Schiantarelli | Last: Rizwan Haq
- Tags: disease | n_authors: 15
(no abstract in metadata)

### Fatty acids in the tumor microenvironment reprogram neutrophils to induce adenosine-mediated immunosuppression in mice.
- Nature Communications | 2026-10-20 | https://doi.org/10.1038/s41467-026-78771-8
- First: Rashi Singhal | Last: Yatrik M Shah (Department of Molecular and Integrative Physiology, University of Michigan, Ann Arbor, MI, USA. shahy@umich.edu.; Rogel Cancer Center, University of Michigan, Ann Arbor, MI, USA. shahy@umich.edu.; Div)
- Tags: disease | n_authors: 29
As solid tumors progress, the tumor microenvironment becomes increasingly immunosuppressive, impairing cytotoxic T-cell activity and limiting the efficacy of immune checkpoint blockade. However, the mechanistic drivers of this immunosuppression remain poorly understood. Here, we identify a tumor-derived lipid-neutrophil-adenosine axis as a critical regulator of immune suppression in advanced colorectal cancer (CRC). We show that fatty acids enriched in tumor interstitial fluid reprogram neutroph...

### Chronic TFE3 activation in TFE3-associated neurodevelopmental disorder drives metabolic rigidity, lysosomal failure, and cell-extracellular matrix destabilization.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78845-7
- First: José A Martina | Last: Rosa Puertollano (Laboratory of Protein Trafficking and Organelle Biology, Cell and Developmental Biology Center, National Heart, Lung, and Blood Institute, National Institutes of Health, Bethesda, MD, USA. puertolr@ma)
- Tags: disease | n_authors: 6
The transcription factor TFE3 coordinates cellular adaptation to stress. While its acute activation is cytoprotective, chronic TFE3 dysregulation is linked to diverse pathologies. Here, we characterize the cellular landscape of TFE3-NDD, a recently described neurodevelopmental disorder caused by mutations that disrupt the TFE3-Rag GTPase interface, leading to constitutive TFE3 nuclear localization. Using patient-derived fibroblasts, we show that TFE3-NDD is primarily a metabolic and homeostatic ...

### Peripheral glia drive the initiation of cutaneous squamous cell carcinoma.
- Nature Communications | 2026-10-20 | https://doi.org/10.1038/s41467-026-78778-1
- First: Sofia Micheli | Last: Lukas Sommer (Institute of Anatomy, University of Zurich, Zurich, Switzerland. lukas.sommer@anatomy.uzh.ch.)
- Tags: disease | n_authors: 19
Although tumor innervation is known to promote cancer progression, underlying mechanisms remain poorly understood and have mostly been linked to axonal signaling. Here, we identify peripheral glia as critical drivers of cutaneous squamous cell carcinoma (cSCC), the second most common skin cancer in humans. Tumor-associated glial cells (TAGs) resemble embryonic Schwann cell lineage stages, are abundant in the stroma of premalignant lesions and established murine and human cSCC, and are essential ...

### Longitudinal ctDNA profiling reveals genomic risk and molecular response to bireociclib in advanced breast cancer.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78782-5
- First: Yan Wang | Last: Binghe Xu (Department of Medical Oncology, National Cancer Center/National Clinical Research Center for Cancer/Cancer Hospital, Chinese Academy of Medical Sciences and Peking Union Medical College, Beijing, Chin)
- Tags: disease | n_authors: 18
Bireociclib plus fulvestrant improves outcomes in hormone receptor-positive, HER2-negative advanced breast cancer, but molecular determinants of benefit and resistance remain unclear. Here we report an exploratory longitudinal circulating tumor DNA (ctDNA) analysis of the randomized phase Ⅲ BRIGHT-2 trial (ClinicalTrials.gov, NCT05077449) in female patients, profiling 596 plasma samples collected at baseline, on treatment, and at end of treatment with a 1,021-gene panel. Detectable baseline ctDN...

### PRMT5 activity sustains histone production to maintain genome integrity.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78671-x
- First: Jacob S Roth | Last: David Shechter (Department of Biochemistry, Albert Einstein College of Medicine, Bronx, NY, USA. david.shechter@einsteinmed.edu.)
- Tags: disease | n_authors: 19
Histone proteins package DNA into nucleosomes, forming chromatin and thereby safeguarding genome integrity. Proper histone expression is essential for cell proliferation and chromatin organization, yet the upstream regulators of histone supply remain incompletely understood. PRMT5, a protein arginine methyltransferase that catalyzes symmetric dimethylation of arginine residues, is frequently overexpressed in cancer and targeted in multiple clinical trials, but its cell-essential function remains...

### Large-scale proteomic characterization reveals clinically relevant subtypes of early-stage papillary thyroid cancer for prognostic prediction.
- Nature Communications | 2026-10-20 | https://doi.org/10.1038/s41467-026-78559-w
- First: Jun Pan | Last: Yijun Wu (Department of Thyroid Surgery, The First Affiliated Hospital, School of Medicine, Zhejiang University, Hangzhou, China. wuwu5925@zju.edu.cn.)
- Tags: disease | n_authors: 17
Papillary thyroid cancer (PTC) has a rising incidence. The majority are diagnosed at an early stage, albeit with a minority exhibiting aggressive tendencies. Given its generally indolent nature, controversy persists regarding the management of early-stage PTCs, particularly surgical intervention and long-term surveillance strategies. Here, we conduct a large-scale proteomic characterization of early-stage PTC based on tumor samples from 797 patients. Proteomic profiling unveils clinically releva...

### Terahertz field-induced giant symmetry modulations in a van der Waals antiferromagnet.
- Nature Communications | 2026-10-20 | https://doi.org/10.1038/s41467-026-78519-4
- First: Sheikh Rubaiat Ul Haque | Last: Aaron M Lindenberg (Department of Materials Science and Engineering, Stanford University, Stanford, CA, USA. aaronl@stanford.edu.; Stanford Institute for Materials and Energy Sciences, SLAC National Accelerator Laborator)
- Tags: disease | n_authors: 22
Strong-field terahertz (THz) excitations enable dynamic control over electronic, lattice and symmetry degrees of freedom in quantum materials. Here, we uncover pronounced terahertz-induced symmetry modulations and coherent phonon dynamics in the van der Waals antiferromagnet MnPS3, in which inversion symmetry is broken by its antiferromagnetic spin configuration. Our time-resolved second harmonic generation measurements reveal long-lived giant oscillations in the antiferromagnetic phase, with am...

### Tumor-intrinsic PTPN12 suppresses anti-tumor immunity in colorectal cancer by restraining a dual epigenetic and cytoskeletal dsRNA sensing program.
- Nature Communications | 2026-10-21 | https://doi.org/10.1038/s41467-026-78487-9
- First: Yachang Huo | Last: Yi Zhang (Biotherapy Center and Cancer Center, the First Affiliated Hospital of Zhengzhou University, Zhengzhou, Henan, China. yizhang@zzu.edu.cn.; Zhongyuan Cell Therapy and Immunotherapy Laboratory, Henan Aca)
- Tags: disease | n_authors: 17
Innate sensing of endogenous double-stranded RNA and the ensuing interferon response are crucial for the efficacy of immune checkpoint inhibition. Microsatellite stable colorectal cancer characteristically lacks this response, remaining immune-refractory with undefined intrinsic regulators. Here, through an in vivo clustered regularly interspaced short palindromic repeats screen, we identify PTPN12 as a physiological barrier that suppresses double-stranded RNA sensing and interferon response. TR...

### Dimeric granzyme-A mediates the specific recognition and cleavage of full-length GSDMB.
- Nature Communications | 2026-10-19 | https://doi.org/10.1038/s41467-026-78435-7
- First: Sai Li | Last: Zhonghua Liu (Hefei National Research Center for Interdisciplinary Sciences at the Microscale, MOE Key Laboratory for Cellular Dynamics, University of Science and Technology of China, Hefei, China. xixiaolu@ustc.ed)
- Tags: disease | n_authors: 9
Gasdermin pores formed by the processed N-terminal domain of gasdermin family members induce pyroptotic cell death and are involved in multiple diseases. Gasdermin B (GSDMB) is cleaved by granzyme-A (GZMA) from killer lymphocytes, triggering pyroptosis in targeted cancer cells to enhance antitumor immunity. Previous research has indicated that the substrate specificity of GZMA is determined by interactions outside the catalytic site, but the molecular mechanism by which the exosite of GZMA recog...

### CD44-DT regulates p21-dependent senescence via interacting with AR-PCNA complex, revealing a therapeutic vulnerability to chimeric ncRNA-mediated AR degradation in prostate cancer
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.17.767372
- First: Hakiminia, F. | Last: Asadi, M. H.
- Corresponding: Malek Hossein Asadi (Institute of Human Genetics)
- Tags: disease | n_authors: 7
Aberrant androgen receptor (AR) signaling driven by androgens plays a critical role in prostate cancer (PCa) progression. Interestingly, bipolar androgen therapy (BAT), a novel therapeutic strategy with cycles between near-castrate and supraphysiological androgen levels (SAL), suppresses PCa growth. SAL induces cellular senescence in various PCa models mediated by the AR, activation of AKT signaling and hypophosphorylation of pRb. Here, we show that SAL upregulates the lncRNA CD44-DT, the CD44 d...

### Doublecortin like kinase 1 (DCLK1) interacts with BRG1 chromatin remodeler and regulates neuronal activity-induced gene activation
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.17.766006
- First: Luo, Y. | Last: Wu, J.
- Corresponding: Jiang Wu (University of Texas Southwestern Medical Center)
- Tags: disease | n_authors: 5
SWI/SNF-like BAF ATP-dependent chromatin remodeling complexes play important roles in neural development and plasticity by regulating neural gene expression, especially in response to neuronal stimulations. Previously, we have shown that BRG1, the core subunit of BAF, undergoes neuronal activity-induced phosphorylation, which is important for the expression of a group of activity regulated genes (ARGs). Proteomic analyses identified Doublecortin like kinase 1 (DCLK1) as a novel BRG1 interacting ...

### ATR coordinates nuclear and cytoskeletal mechanics during leukemic migration
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767255
- First: Armesto, M. | Last: Redondo Munoz, J.
- Corresponding: Javier Redondo Munoz (Centro de Investigaciones Biologicas Margarita Salas, CIB Margarita Salas-CSIC)
- Tags: disease | n_authors: 10
Mechanical adaptation is essential for tumor cells to cross physical barriers during dissemination, but the mechanisms linking genome-stress signalling to cellular mechanics remain poorly understood. Here, we demonstrate that ATR (ataxia telangiectasia and Rad3-related kinase) acts as a dual regulator of nuclear and cytoskeletal adaptations in T-cell acute lymphoblastic leukemia (T-ALL). Genetic depletion or pharmacological inhibition of ATR altered nuclear architecture and mechanical behaviour,...

### NXP800 suppresses HSF1 through coordinated stress signaling and GCN2-dependent translational repression in glioblastoma
- biorxiv | 2026-11-18 | https://doi.org/10.64898/2026.11.17.764637
- First: DeHart, H. | Last: Carpenter, R.
- Corresponding: Richard Carpenter (Indiana University)
- Tags: disease | n_authors: 6
Under states of proteotoxic stress, Heat Shock Factor 1 (HSF1) serves as the primary transcription factor responsible for restoring protein homeostasis. General Control Nonderepressible 2 (GCN2) similarly alleviates cellular stress. Activated by a shortage in amino acids, GCN2 triggers the phosphorylation of eIF2 to downregulate global protein synthesis while selectively translating survival-promoting proteins like Activating Transcription Factor 4 (ATF4). Cancer cells often exploit these pathwa...

### SHMT1 and SHMT2 inhibition disrupts metabolic adaptation in glioblastoma
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767126
- First: Schroeder, J.-H. | Last: Luger, A.-L.
- Corresponding: Anna-Luisa Luger (Dr. Senckenberg Institute of Neurooncology, University Hospital Frankfurt, Goethe University, Frankfurt am Main, Germany)
- Tags: disease | n_authors: 19
Glioblastoma cells adapt to hypoxia and nutrient restriction through metabolic reprogramming. Serine hydroxymethyltransferases 1 and 2 (SHMT1, SHMT2) channel serine-derived one carbon units into folate metabolism, linking biosynthesis, respiration and redox defence. Its contribution to tumour metabolic homeostasis and adaptation to hypoxia and nutrient restriction remains unclear. We combined dual pharmacological SHMT inhibition using (+)-SHIN1 in glioblastoma cell lines, including patient-deriv...

### Novel selective CDK4-inhibitor ALK-13743: Functional determinants of response in ER+ breast cancer models
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767343
- First: Kumarasamy, V. | Last: Knudsen, E. S.
- Corresponding: Erik S Knudsen (Roswell Park Comprehensive Cancer Center)
- Tags: disease | n_authors: 12
Background: Cyclin-dependent kinase 4 (CDK4) and CDK6 are central drivers of cell cycle progression in estrogen receptor-positive (ER+) breast cancer, and pharmacological inhibition of this pair has become a standard-of-care therapeutic strategy. However, currently approved CDK4/6 inhibitors palbociclib, ribociclib, and abemaciclib carry associated toxicities, including myelosuppression and other adverse effects which are associated with inhibition of CDK6 that limits tolerability and combinator...

### Epithelial network percolation reshapes collective mechanochemical dynamics and modes of competitive cell elimination
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767171
- First: Nayak, A. | Last: Hirashima, T.
- Corresponding: Tsuyoshi Hirashima (Mechanobiology Institute, National University of Singapore, Singapore; Department of Physiology, Yong Loo Lin School of Medicine, National University of Singapo)
- Tags: disease | n_authors: 7
Living tissues are active materials whose collective states depend on mechanochemical communication across connected cells. Yet tissues undergoing repair, ageing or tumorigenesis often contain intermingled cells with divergent states. How such heterogeneity alters tissue-scale communication, and whether cell competition can restore it, remains unclear. Here we track ERK activity, a dynamic readout and regulator of epithelial mechanochemical coupling, to ask how tissues recover from an aberrant s...

### Saruparib recapitulates PARP-BRCA synthetic lethality with PARP1-trapping properties limiting its cytotoxicity
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.17.767429
- First: Nakano, S. | Last: Murai, J.
- Corresponding: Junko Murai (Department of Cell Growth and Tumor Regulation, Proteo-Science Center, Premier Institute for Advanced Studies, Ehime University, Toon, Ehime, 791-0295, Japan)
- Tags: disease | n_authors: 14
The original concept of PARP synthetic lethality proposes that loss of poly(ADP-ribose) polymerase (PARP) activity selectively kills homologous recombination (HR)-deficient cells. However, clinically approved PARP1/2 inhibitors (PARPis) are used at exposures exceeding those required for catalytic inhibition. At these doses, PARP trapping is cytotoxic to HR-proficient cells and limits the therapeutic window in HR-deficient cancers. Saruparib has been developed as a PARP1-selective inhibitor to re...

### YAP1-induced super-enhancer rewiring mediates gene-environment-driven malignant reprogramming and metastatic ecosystem formation in head and neck cancer
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.15.766730
- First: Higashihara, M. | Last: Masuda, M.
- Corresponding: Muneyuki Masuda (National Hospital Organization Kyushu Cancer Center)
- Tags: disease | n_authors: 18
Head and neck squamous cell carcinoma (HNSCC) is characterized by frequent TP53 mutations, which are insufficient for tumorigenesis and largely undruggable, underscoring the need to define epigenetic mechanisms driving cancer evolution. Here we show that TP53 mutation facilitates YAP1-dependent transcriptional reprogramming, driving epigenetic tumor evolution by hijacking tissue-regenerative programs. Integrated multi-omics analyses of mouse models and multiregional human HNSCC samples reveal th...

### MUC4 regulatory-region methylation is remodeled during breast cancer progression and metastasis
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.11.765423
- First: Free, S. R. | Last: Carraway, K. L.
- Corresponding: Kermit L Carraway III (University of California Davis School of Medicine)
- Tags: disease | n_authors: 5
Background Mucin-4 (MUC4) contributes to tumor cell survival and metastatic behavior, but its expression in breast cancer is unusual; previous studies have demonstrated that MUC4 levels are reduced in primary tumors relative to normal epithelium but are partially restored in metastatic lesions. Because DNA methylation is known to regulate MUC4 gene expression in cultured cancer cells, we investigated whether methylation of the MUC4 regulatory region changes across breast cancer progression. Resu...

### Development of a high-throughput protein array to discover selective dsRNA binding domain interactions
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767677
- First: Zehrbach, N. | Last: Ishak, C. A.
- Corresponding: Charles Allan Ishak (University of Texas MD Anderson Cancer Center)
- Tags: disease | n_authors: 7
Endogenous double stranded RNAs (dsRNAs) function as signal transduction molecules through interactions with host proteins. These interactions can induce signaling cascades implicated in normal homeostasis and diseases such as cancer. Therefore, the discovery of interactions between dsRNAs and dsRNA binding proteins (dsRBPs) is critical for comprehensive elucidation of signal transduction cascades. Discovery of dsRNA-dsRBP interactions remains hindered due to technical limitations that can inclu...

### Combined JAK2 and HSP90 inhibition produces synergistic anti-tumour activity across preclinical glioblastoma models
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767500
- First: Furqan, M. | Last: Carragher, N. O.
- Corresponding: Neil O Carragher (University of Edinburgh)
- Tags: disease | n_authors: 22
Background: Glioblastoma (GBM) remains difficult to treat because of tumour heterogeneity and the limited activity of single-target therapies. Our previous phenotypic drug screen identified JAK2/STAT3 signalling and HSP90-dependent protein homeostasis as pharmacological vulnerabilities. We investigated whether combined JAK2 and HSP90 inhibition could produce broader anti-tumour activity across GBM models. Methods: Multiple JAK2 and HSP90 inhibitors were tested alone and in combination across 2- ...

### Low serine-glycine-one-carbon pathway activity defines purine salvage dependence in neuroblastoma
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767701
- First: Ding, J. | Last: Ding, H.-F.
- Corresponding: Han-Fei Ding (University of Alabama at Birmingham, Birmingham, AL)
- Tags: disease | n_authors: 6
MYCN amplification promotes serine-glycine-one-carbon (SGOC) metabolism in neuroblastoma, creating an intrinsic difference in SGOC activity between MYCNamplified and non-MYCN-amplified high-risk tumors. This metabolic distinction provides a model to investigate how SGOC activity shapes purine metabolism. Here, we show that non-MYCN-amplified neuroblastoma cell lines exhibit lower SGOC pathway activity and are more resistant to pharmacologic suppression of SGOC metabolism by SHMT inhibition under...

### Radiation survival selects clonally restricted NSCLC survivors with impaired metastatic capacity and distinct bioenergetic states
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767282
- First: Martinez-Cruz, M. | Last: Grüner, B. M.
- Corresponding: Barbara M Grüner (West German Cancer Center, Department of Medical Oncology, Cell Plasticity and Metastasis, University of Duisburg-Essen, Germany; German Cancer Consortium (DKTK)
- Tags: disease | n_authors: 12
Radiation resistance and recurrence remain major challenges in non-small cell lung cancer (NSCLC). Whether radiation survival enriches for more aggressive, metastasis-competent cells remains unresolved. Using longitudinal cellular barcoding, functional assays, and multi-omics profiling in diverse NSCLC models, we show that fractionated irradiation imposes a strong clonal bottleneck, but recovery follows either stochastic or deterministic trajectories. Despite this diversity, all radiation-surviv...

### Connexin43 drives mitochondrial biogenesis and organelle stress in BRAF-mutant melanoma cells
- biorxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.18.767001
- First: Guitian-Caamano, A. | Last: Mayan, M. D.
- Corresponding: María D. Mayán (CellCOM Research Group, Center for Research in Nanomaterials and Biomedicine (CINBIO), University of Vigo, Vigo, Spain)
- Tags: disease | n_authors: 10
Metabolic flexibility helps cancer cells survive targeted therapy, and BRAF-mutant melanoma rewires mitochondrial metabolism in response to BRAF/MEK inhibitors (BRAF/MEKi). We previously showed that connexin43 (Cx43) acts as a tumour suppressor in BRAF-mutant melanoma and enhances the response to BRAF/MEKi. Here, we investigated whether mitochondrial remodelling contributes to these effects. Cx43 upregulation promoted mitochondrial biogenesis including selective increase of CI and CV, enhanced o...

### Transcriptomic and Genomic Sequencing of South African Colorectal Cancer Patients Reveal Population-Specific Insights and Variants
- medrxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.19.26368287
- First: Kader, Z. | Last: Kaur, M.
- Corresponding: Mandeep Kaur (University of the Witwatersrand)
- Tags: disease | n_authors: 7
Colorectal cancer (CRC) genomic studies have largely underrepresented African populations, limiting understanding of disease biology in these groups. This study addressed this gap by generating integrated genomic and transcriptomic data from South African (SA) CRC patients, establishing a foundation for future cancer studies. Bulk RNA sequencing of 32 samples identified several differentially expressed genes between tumour and normal samples, with AGAP3, AMPD2, ANKRD10, and SALL4 showing strong ...

### Excess of de novo substitutions in the genomes of individuals with newly acquired germline TP53 mutations
- medrxiv | 2026-11-19 | https://doi.org/10.64898/2026.11.19.26364643
- First: Parmentier, M. | Last: Wang, W.
- Corresponding: Wenyi Wang (Department of Bioinformatics and Computational Biology, The University of Texas MD Anderson Cancer Center, Houston, TX, USA)
- Tags: disease | n_authors: 10
Inherited defects in the tumour suppressor gene TP53 cause Li-Fraumeni syndrome, a highly penetrant predisposition to childhood and adult cancers. About half of affected individuals carry a variant absent from both parents, and these are the patients missed by family-history-based testing criteria. Where and when such variants arise, in which parental gamete or after fertilisation, remains unresolved, as primary family data are scarce. We addressed this using whole-genome and linked-read sequenc...

## No keyword hits (203)

- Nature | People entering old age now have better memory than their parents did | last: Miryam Naddaf | https://doi.org/10.1038/d41586-026-03783-9
- Nature | Bacteria and viruses team up to hasten the demise of algal blooms | last:  | https://doi.org/10.1038/d41586-026-03606-x
- Nature | AI is ditching hallucinated references — and other bad habits | last: Kaia Glickman | https://doi.org/10.1038/d41586-026-03753-1
- Nature | Anthropic IPO: four ways the AI giant wants to disrupt science | last: Heidi Ledford | https://doi.org/10.1038/d41586-026-03788-4
- Nature | Calcium catalysed nucleophilic fluorination | last: Simon Aldridge | https://doi.org/10.1038/s41586-026-11445-z
- Nature | Daily briefing: How vampire bats survive on blood alone | last: Flora Graham | https://doi.org/10.1038/d41586-026-03780-y
- Nature | Sore throat? The brain has surprising control over how ill you feel | last: Max Kozlov | https://doi.org/10.1038/d41586-026-03774-w
- Nature | More tropical cyclones hit peak fury at the worst possible time | last:  | https://doi.org/10.1038/d41586-026-03748-y
- Nature | AI is turbocharging cyberattacks — can computer scientists catch up? | last: David Adam | https://doi.org/10.1038/d41586-026-03775-9
- Nature | Daily briefing: Can you spot the ‘tortured phrases’? | last: Flora Graham | https://doi.org/10.1038/d41586-026-03791-9
- Nature | University students are biggest spreaders of COVID | last: Heidi Ledford | https://doi.org/10.1038/d41586-026-03746-0
- Science | Killing more sea lions won’t help endangered salmon recover, model suggests | last: Erik Stokstad | https://doi.org/10.1126/science.aeo2675
- Science | Zero-shot de novo design of a metalloenzyme | last: Po-Ssu Huang | https://doi.org/10.1126/science.aej3009
- Science | AI rivals take on one of physics’ hardest math problems | last: Jacklin Kwan | https://doi.org/10.1126/science.aeo2673
- Science | Elastic-field reorganization stabilizes soft-lattice perovskites for durable solar cells | last: Deren Yang | https://doi.org/10.1126/science.aeh3114
- Science | Ghost chemicals | last: Perri Thaler | https://doi.org/10.1126/science.aeo2671
- Science | The power of feedback | last: Sasan Jalili | https://doi.org/10.1126/science.aeo2220
- Science | Bumble bee cognition | last: Stanley Heinze | https://doi.org/10.1126/science.aek1724
- Science | DOE to delay atom smasher and speed AI, quantum, and fusion projects | last: Adrian Cho | https://doi.org/10.1126/science.aeo2674
- Science | Pinpointing planned speech | last: Adeen Flinker | https://doi.org/10.1126/science.aem7976
- Science | Atmospheric organic nitrogen is a major nutrient source to global oceans | last: Jian Zhen Yu | https://doi.org/10.1126/science.aeg4265
- Science | The scientific record is never finished | last: Valda Vinson | https://doi.org/10.1126/science.aen9176
- Science | Quantum-classical separation in bounded-resource tasks arising from measurement contextuality | last: M. Devoret | https://doi.org/10.1126/science.aec3042
- Science | Measles comeback in U.S. adds to global resurgence | last: Gretchen Vogel | https://doi.org/10.1126/science.aeo2672
- Science | Divergent activation of the RXFP1 relaxin receptor by protein and small-molecule agonists | last: Andrew C. Kruse | https://doi.org/10.1126/science.aei0135
- Science | Chinese gene-therapy researchers fired after probe into child’s death | last: Brendan Borrell | https://doi.org/10.1126/science.aeo2676
- Science | Molecular adhesion for durable metal halide perovskite modules | last: Xiaopeng Zheng | https://doi.org/10.1126/science.aej5001
- Science | In Other Journals | last: Angela Hessler | https://doi.org/10.1126/science.aeo2219
- Science | Digital doubles and the modern crisis of identity | last: K. Paige Harden | https://doi.org/10.1126/science.ael6252
- Science | Making ecological programs work at scale | last: Yuanning Liang | https://doi.org/10.1126/science.aen0206
- Science | Disclose trade-offs in US emissions rule change | last: Randall Lutter | https://doi.org/10.1126/science.aem5489
- Science | Widespread marine mammal and seabird reductions are unlikely to benefit salmon due to indirect ecosystem effects | last: Joshua D. Stewart | https://doi.org/10.1126/science.aeb1122
- Science | Telemetric calorimetry for wireless continuous reaction profiling | last: Song Lin | https://doi.org/10.1126/science.aei7840
- Science | The fate of poised pre-mRNAs shapes mitochondrial activity and cellular differentiation | last: Lynne E. Maquat | https://doi.org/10.1126/science.aee8018
- Science | A quantum paradox at work | last: Rui Soares Barbosa | https://doi.org/10.1126/science.aem4000
- Science | A thalamo-amygdalar circuit drives female vulnerability to chronic pain after early-life stress | last: Sebastian Wieland | https://doi.org/10.1126/science.adx5757
- Science | Save scientific terminology from executive orders | last: Zhiguang Chen | https://doi.org/10.1126/science.aen0458
- Science | Quaternary carbon–guided carbocation cascade rearrangement to enantioenriched polycycles | last: Wen-Bo Liu | https://doi.org/10.1126/science.aei2041
- Science | Interpenetrating bottlebrush elastomer for low-loss soft ultrasonic interfaces | last: Xuanhe Zhao | https://doi.org/10.1126/science.aef9553
- Science | Angular momentum transfer from an optical vortex to an atomic rotor | last: Hartmut Häffner | https://doi.org/10.1126/science.aeh0182
- Science | Rising risk of deforestation in Indonesia’s pulp sector | last: David Gaveau | https://doi.org/10.1126/science.aeb9995
- Science | Quiet within, chaos without: Turbulence shelters drive selective particle capture and release | last: William T. M. Irvine | https://doi.org/10.1126/science.aee9889
- Science | Meso–microporous zeolitic materials with thin walls containing ordered 10-ring channels | last: Jian Li | https://doi.org/10.1126/science.aei6161
- Science | A neural code for generative speech production in human Wernicke’s area | last: Edward F. Chang | https://doi.org/10.1126/science.aef8963
- Science | In Science Journals | last: Jelena Stajic | https://doi.org/10.1126/science.aeo2218
- Science | Mammalian development, recorded and decoded | last: Nozomu Yachie | https://doi.org/10.1126/science.aem7343
- Science | Beyond containment in insect farming | last: Miao Li | https://doi.org/10.1126/science.aem5274
- Science | A DNA Typewriter records the cell lineage history of a mouse, from zygote to late organogenesis | last: Jay Shendure | https://doi.org/10.1126/science.ael0508
- Cell | Myelin pathology is a key feature of X-linked dystonia-parkinsonism | last: Shane A. Liddelow | https://doi.org/10.1016/j.cell.2026.10.046
- Cell | Genome writing reveals SVA retrotransposon consequences in X-linked dystonia-parkinsonism | last: Jef D. Boeke | https://doi.org/10.1016/j.cell.2026.07.057
- Cell | Genomic surveillance reveals age-structured SARS-CoV-2 transmission across settings | last: Pardis C. Sabeti | https://doi.org/10.1016/j.cell.2026.10.051
- Cell | CD19 CAR T cell therapy alters disease-associated immune signatures in multiple sclerosis | last: Manuel A. Friese | https://doi.org/10.1016/j.cell.2026.10.044
- Cell | A natural mutation of timeless enhances mosquito thermal adaptation and malaria parasite transmission | last: Sibao Wang | https://doi.org/10.1016/j.cell.2026.10.049
- Cell | RNA folding drives species-dependent host mRNA partitioning in Ebola virus condensates | last: Erica Ollmann Saphire | https://doi.org/10.1016/j.cell.2026.10.047
- Nature Methods | Space-map is a tool that integrates tissue slices into detailed 3D cell maps | last:  | https://doi.org/10.1038/s41592-026-03309-1
- Nature Methods | 4D ultrasound cerebral angiography reveals the hemodynamics of the circle of Willis in primates | last: Clément Papadacci | https://doi.org/10.1038/s41592-026-03314-4
- Nature Methods | Scalable electron tomography for connectomics | last: Wei-Chung Allen Lee | https://doi.org/10.1038/s41592-026-03345-x
- Nature Biotechnology | Programmable functional RNA design with a virtual scientist | last: Yu Li | https://doi.org/10.1038/s41587-026-03362-3
- Nature Genetics | Tracing genetic risk of neurodegenerative disease through variants affecting microglial function | last:  | https://doi.org/10.1038/s41588-026-02839-w
- Nature Medicine | Expansion and cytotoxicity of mucosal CAR+ T cells in enterocolitis associated with BCMA CAR-T cell therapy | last: Mark P. Hamilton | https://doi.org/10.1038/s41591-026-04731-w
- Nature Medicine | Multicenter characterization of enterocolitis associated with BCMA-directed CAR T cell therapy | last: Jeffrey L. Wolf | https://doi.org/10.1038/s41591-026-04783-y
- Nature Medicine | Harnessing smartwatches to spot undiagnosed hypertension | last: Karen O’Leary | https://doi.org/10.1038/d41591-026-00058-8
- Nature Communications | Harnessing regioselective aryl migration of pyridone-based aryl-λ3-iodonium salts to access iodine-substituted aryloxypyridines | last: Shaoyu Mai | https://doi.org/10.1038/s41467-026-79356-1
- Nature Communications | Greenland ice sheet retreat intensifies the African monsoon through a polar-tropical atmospheric teleconnection | last: Qiong Zhang | https://doi.org/10.1038/s41467-026-79541-2
- Nature Communications | Evolutionary plasticity of bacterial surface layer protein exoskeletons | last: Kacper M. Sendra | https://doi.org/10.1038/s41467-026-77977-0
- Nature Communications | Disturbance increases soil microbiome functional redundancy but decreases capacity for insurance via winnowed environmental responsiveness | last: Ashley Shade | https://doi.org/10.1038/s41467-026-79487-5
- Nature Communications | A metal ion-assisted workflow for practical and scalable enrichment of small extracellular vesicles from biofluids | last: Qinglin Li | https://doi.org/10.1038/s41467-026-79613-3
- Nature Communications | Facial photographs reveal mortality risk beyond triage and clinical risk scores | last: Rasmus Bo Hasselbalch | https://doi.org/10.1038/s41467-026-79581-8
- Nature Communications | Early face-experience deprivation leads to long-lasting deficits in macaque cortical face processing | last: Margaret S. Livingstone | https://doi.org/10.1038/s41467-026-79612-4
- Nature Communications | Interfacial mechanisms of gas-bubble friction | last: Hongbo Zeng | https://doi.org/10.1038/s41467-026-79472-y
- Nature Communications | Impacts of medications for obesity on global health and the environment | last: Peter Alexander | https://doi.org/10.1038/s41467-026-79412-w
- Nature Communications | Protecting-group-lean platform for synthesizing diverse phenylethanoid glycosides uncovers antifibrotic leads | last: Yugen Zhu | https://doi.org/10.1038/s41467-026-79652-w
- Nature Communications | Trypanosomes Maintain Propulsion in Confined Environments by Modulating Rotational Motility from Swimming to Network-Threading Propulsion | last: Markus Engstler | https://doi.org/10.1038/s41467-026-79874-y
- Nature Communications | Bicyclo[2.1.1]hexanes as saturated bioisosteres of meta-benzene | last: Pavel K. Mykhailiuk | https://doi.org/10.1038/s41467-026-79402-y
- Nature Communications | Governing cryospheric risk beyond political timeframes | last: Anu Lähteenmäki-Uutela | https://doi.org/10.1038/s41467-026-79617-z
- Nature Communications | Twist-engineered arbitrary polarization detection for intelligent polarimetric sensing | last: Jing Zhou | https://doi.org/10.1038/s41467-026-79650-y
- Nature Communications | Atomically ordered few-layer molybdenum boride MBenes for enhanced electromagnetic response | last: Renchao Che | https://doi.org/10.1038/s41467-026-79512-7
- Nature Communications | A defence-in-depth strategy for securing AI-driven biological sequence design | last: Georges Hattab | https://doi.org/10.1038/s41467-026-78758-5
- Nature Communications | Parental leave benefits and fathers’ postpartum mental health in Sweden | last: Sol P. Juárez | https://doi.org/10.1038/s41467-026-79284-0
- Nature Communications | Numerosity is directly sensed and dynamically transformed in the human brain | last: Manuela Piazza | https://doi.org/10.1038/s41467-026-79330-x
- Nature Communications | Bordetella pertussis adapts to human nasal mucosa through biofilm-associated virulence reprogramming and host-defense attenuation | last: Rajendar Deora | https://doi.org/10.1038/s41467-026-79522-5
- Nature Communications | Droplet-Assisted Growth of Re-Entrant Micro-Mushroom Surfaces with Switchable Superhydrophobicity and Adhesive Resistance | last: Stefan Seeger | https://doi.org/10.1038/s41467-026-79389-6
- Nature Communications | Asymmetric coordination triggers dual-site synergy in gold nanoclusters for efficient aerobic oxidation | last: Xian-Kai Wan | https://doi.org/10.1038/s41467-026-79369-w
- Nature Communications | Modulating FCC/HCP phase boundaries in inverse Co@BOx catalysts via crystal-phase-ratio variation for propane oxidative dehydrogenation | last: Siyu Yao | https://doi.org/10.1038/s41467-026-79394-9
- Nature Communications | Quantum sensing-enabled deuterium NMR spectroscopy with nanoscale sensitivity at low magnetic fields | last: Dominik B. Bucher | https://doi.org/10.1038/s41467-026-78803-3
- Nature Communications | Vertically aligned dual-channel metal-organic framework nanosheet membranes for gas separation | last: Haihui Wang | https://doi.org/10.1038/s41467-026-77853-x
- Nature Communications | Designing 3D oxygen–diffusion scaffolds for high-performance metal fuels | last: Hexi Baoyin | https://doi.org/10.1038/s41467-026-79710-3
- Nature Communications | Rapid and selective metal-free O2 reduction to H2O2 using a molecular CpN3 electrocatalyst | last: Demyan E. Prokopchuk | https://doi.org/10.1038/s41467-026-79096-2
- Nature Communications | Macrophage-exacerbated viral lung injury and mechanical overdistension-driven bacterial superinfection replicated in a human lung chip | last: Donald E. Ingber | https://doi.org/10.1038/s41467-026-78889-9
- Nature Communications | Hybrid-parity sliding multiferroics | last: Xiaotian Wang | https://doi.org/10.1038/s41467-026-79435-3
- Nature Communications | Lanthanide-dependent methanotroph thrives on radioactive promethium | last: Lena J. Daumann | https://doi.org/10.1038/s41467-026-79368-x
- Nature Communications | Coherence toroidal vortices and statistic-veiled correlation topologies | last: Xin Liu | https://doi.org/10.1038/s41467-026-78404-0
- Nature Communications | Large electrocaloric effects in unannealed multilayer capacitors of partially ordered lead scandium tantalate | last: Neil D. Mathur | https://doi.org/10.1038/s41467-026-79481-x
- Nature Communications | Symmetry-breaking antibody binding reveals extensive capsid malleability in pandemic human norovirus | last: B. V. Venkataram Prasad | https://doi.org/10.1038/s41467-026-79222-0
- Nature Communications | Automated data to model transformation for constraint programming with AI | last: Liang Gao | https://doi.org/10.1038/s41467-026-78715-2
- Nature Communications | Hyperelastic microfibers as bioinspired proprioceptive artificial muscles | last: Seongjun Park | https://doi.org/10.1038/s41467-026-79467-9
- Nature Communications | Atom-level pinning effect reinforced electrooxidative coupling of anilines into azos | last: Hu Li | https://doi.org/10.1038/s41467-026-79417-5
- Nature Communications | SMC5/6 safeguards chromatin compartments and TAD boundaries for genome stability | last: Dana Branzei | https://doi.org/10.1038/s41467-026-79493-7
- Molecular Cell | The METTL orchestra plays on a loop, keeping the volume just right | last: Pedro J. Batista | https://doi.org/10.1016/j.molcel.2026.10.030
- Molecular Cell | When two become one: Chimeric RNAs regulating innate immunity | last: Thirumala-Devi Kanneganti | https://doi.org/10.1016/j.molcel.2026.10.032
- Molecular Cell | Synthetic viability: FANCM loss enhances the fitness of BRCA2 mutant cells | last: Roger A. Greenberg | https://doi.org/10.1016/j.molcel.2026.10.026
- Molecular Cell | Beneath the surface: Hidden degrons and untapped ligases for molecular glue degrader discovery | last: Olle Sangfelt | https://doi.org/10.1016/j.molcel.2026.10.028
- Molecular Cell | Amyloid couriers for the sperm RNA code | last: Qi Chen | https://doi.org/10.1016/j.molcel.2026.10.029
- Neuron | The neural mechanisms of fast versus slow decision-making | last: Matthew E. Larkum | https://doi.org/10.1016/j.neuron.2026.10.024
- Genome Biology | Dynamic changes in mRNA isoform usage during human retinal organoid development | last: Donald Zack | https://doi.org/10.1186/s13059-026-04354-x
- Genome Biology | Evolution of plant genome architecture: a decade of progress | last: Rod A. Wing | https://doi.org/10.1186/s13059-026-04344-z
- Genome Biology | Inherent specificity and variation sensitivity as quantitative metrics for RNA binding proteins | last: Joseph M. Luna | https://doi.org/10.1186/s13059-026-04352-z
- Genome Biology | Naturally occurring variation in gene-associated transposable elements impacts gene expression and phenotypic diversity in woodland strawberry | last: Pablo A. Manavella | https://doi.org/10.1186/s13059-026-04345-y
- NEJM | Slightly Alive — Improving Antituberculosis Therapy | last: Eric J. Rubin | https://doi.org/10.1056/nejme2614653
- NEJM | Assessing Multiple Treatment Regimens for Tuberculosis | last: Michael Hoelscher | https://doi.org/10.1056/nejmoa2611913
- Genome Biology | Benchmarking generative AI tools for literature retrieval and summarization in genomic variant interpretation. | last: Paolo Magni | https://doi.org/10.1186/s13059-026-04237-1
- Nature Communications | Baseline radiographic and microbiologic predictors of treatment outcomes in a shortened all-oral regimen for MDR/RR-TB. | last: Kunda Kwabisha Mikanda | https://doi.org/10.1038/s41467-026-78700-9
- Nature Communications | A 700-kilometre copper supply network in Bronze Age China revealed by multi-proxy ore fingerprinting. | last: Siran Liu | https://doi.org/10.1038/s41467-026-78864-4
- Nature Communications | Identification and genetic characterization of megabase-scale plasmids of Enterobacteriaceae. | last: Jillian F Banfield | https://doi.org/10.1038/s41467-026-78742-z
- Nature Communications | Divergent anaerobic fates of biodegradable plastics in landfill leachate. | last: Jaewook Myung | https://doi.org/10.1038/s41467-026-78850-w
- Nature Communications | Human hemoglobin protects the parasite cytoskeleton during Plasmodium falciparum gametocyte development. | last: Rui Zhang | https://doi.org/10.1038/s41467-026-78694-4
- Nature Communications | Field-induced near-unity spin polarization in a highly emissive organic diradical. | last: Geyu Lu | https://doi.org/10.1038/s41467-026-78882-2
- Nature Communications | Hydrogen-stabilized dual-phase architecture enables ductility in refractory molybdenum nanowires. | last: Jianbo Wang | https://doi.org/10.1038/s41467-026-79244-8
- Nature Communications | A prefrontal-bed nucleus pathway controls aversive memory specificity independently of glucocorticoids. | last: Jason J Radley | https://doi.org/10.1038/s41467-026-78719-y
- Nature Communications | Thermal sculpting of nanoconfined single-atom cavities enables urea electrosynthesis with near-unity selectivity. | last: Qingsong Hua | https://doi.org/10.1038/s41467-026-79024-4
- Nature Communications | Concentration‑dependent switching between ligand‑like and solvent‑like lipid regulation in a model ion channel. | last: Philipp A M Schmidpeter | https://doi.org/10.1038/s41467-026-78779-0
- Nature Communications | Kinetic acceleration of phosphate remediation in dilute aquatic environments via photovoltaic-driven solid-state electrolyte electrocoagulation. | last: Hong Chen | https://doi.org/10.1038/s41467-026-78830-0
- Nature Communications | dITP shifts the assembly equilibrium of Kongming to activate NAD+ hydrolysis. | last: Tian-Min Fu | https://doi.org/10.1038/s41467-026-78725-0
- Nature Communications | Orbital coupling effect enables low-chloride concentration electrolyte for four-electron redox in aqueous zinc | |iodine batteries. | last: Bingang Xu | https://doi.org/10.1038/s41467-026-78918-7
- Nature Communications | Oncogenic signalling and host immunocompetency govern senescent cell clearance and systemic inflammation in a mouse model of oncogene-induced senescence. | last: Eugenio Montini | https://doi.org/10.1038/s41467-026-79038-y
- Nature Communications | Structural basis of TACO1 function in mitochondrial translation elongation. | last: Joanna Rorbach | https://doi.org/10.1038/s41467-026-78692-6
- Nature Communications | Low-valine diet ameliorates pathological cardiac hypertrophy by inhibiting LONP1-mediated degradation of ATP5F1B in male rodents. | last: Yuehui Yin | https://doi.org/10.1038/s41467-026-78676-6
- Nature Communications | Plasma eMTBR-tau243 and p-tau205 as T2 biomarkers for biological staging and prognosis in Alzheimer's disease. | last: Sang Won Seo | https://doi.org/10.1038/s41467-026-78582-x
- Nature Communications | Metabolic engineering and deep learning-driven protein engineering for N-Acetylneuraminic acid biosynthesis in Escherichia coli. | last: Jin-Song Shi | https://doi.org/10.1038/s41467-026-77406-2
- Nature Communications | Ethnoracial disparities in emergency department triage are more pronounced in lower-risk visits: a multicenter study. | last: William G La Cava | https://doi.org/10.1038/s41467-026-78526-5
- Nature Communications | Crystallization-mediated twisting of supramolecular nanoribbons from plant-derived triterpenes. | last: Orlando J Rojas | https://doi.org/10.1038/s41467-026-78594-7
- Nature Communications | Universal platform for rapid green surface functionalization of diverse porous membranes for sustainable water treatment. | last: Juan Yi | https://doi.org/10.1038/s41467-026-78651-1
- Nature Communications | Sudden collapse of ice mélange under increasing submarine melt at tidewater glaciers. | last: Justin C Burton | https://doi.org/10.1038/s41467-026-78423-x
- Nature Communications | A dynamically tunable diamine ligand enables Cu-catalyzed enantioselective nucleophilic substitution at P(V). | last: Ming Shang | https://doi.org/10.1038/s41467-026-75855-3
- Nature Communications | A prophage-encoded anti-phage defence system that prevents DNA packaging by targeting the terminase complex. | last: Anat A Herskovits | https://doi.org/10.1038/s41467-026-78609-3
- Nature Communications | Exploring healthy aging through preclinical Alzheimer disease in the Knight Alzheimer Research Imaging dataset. | last: Tammie L S Benzinger | https://doi.org/10.1038/s41467-026-78439-3
- Nature Communications | Preferred evolutionary routes of convergence in Klebsiella pneumoniae favor siderophore acquisition over hypervirulence. | last: Francois Lebreton | https://doi.org/10.1038/s41467-026-78501-0
- Nature Communications | Spatiotemporal analysis of insecticide-treated bednet coverage, age and type in Africa from 2006-2024. | last: Peter W Gething | https://doi.org/10.1038/s41467-026-78456-2
- biorxiv | An open-source semi-automated workflow for multi-omics sample extraction | last: Gritsenko, M. A. | https://doi.org/10.64898/2026.11.17.767423
- biorxiv | nf-core/pairgenomealign: a scalable pipeline for pairwise whole-genome alignment | last: Luscombe, N. M. | https://doi.org/10.64898/2026.11.18.767494
- biorxiv | Quantification of cannabidiolic acid in Cannabis sativa using a two-component allosteric protein biosensor | last: Behrendorff, J. B. | https://doi.org/10.64898/2026.11.17.767439
- biorxiv | A modular workflow for biomedical entity normalization across heterogeneous biological ontologies | last: Chagoyen, M. | https://doi.org/10.64898/2026.11.17.767229
- biorxiv | Visual Search and ASD: Basic vs. Superordinate Category Search | last: Hochstein, S. | https://doi.org/10.64898/2026.11.17.767228
- biorxiv | Unified CEBRA learns shared neural latents across recordings to map single-neuron contributions to population codes | last: Mathis, M. W. | https://doi.org/10.64898/2026.11.18.767506
- biorxiv | Dissociable patterns of neurophysiological alterations during guided search in schizophrenia and autism: Evidence from fixation-related potentials, alpha modulation, and functional MRI. | last: Javitt, D. C. | https://doi.org/10.64898/2026.11.17.767357
- biorxiv | Keratinocyte IL-17RA signaling promotes neutrophil recruitment and clinical lesions in experimental epidermolysis bullosa | last: Deng, F. | https://doi.org/10.64898/2026.11.18.767503
- biorxiv | An atlas of the sRNAs and their targets in Staphylococcus aureus | last: Georg, J. | https://doi.org/10.64898/2026.11.17.767300
- biorxiv | Modelling Maternal-to-Zygotic Transition Dynamics to Identify Common Gene Expression Baselines in Zebrafish Development. | last: Focks, A. | https://doi.org/10.64898/2026.11.17.767246
- biorxiv | New medium for the production of Dermacentor reticulatus and Ixodes persulcatus tick primary cell lines | last: V., K. A. | https://doi.org/10.64898/2026.11.17.767464
- biorxiv | Activity-based fluorescence screening uncovers host enzymatic responses to SARS-CoV-2 infection | last: Urano, Y. | https://doi.org/10.64898/2026.11.17.766338
- biorxiv | Disentangling genomic imprinting from indirect parental genetic effects on the human methylome | last: Robinson, M. R. | https://doi.org/10.64898/2026.11.18.767489
- biorxiv | Generation of a Public Dataset for Etiological Subtyping with the Genomic Cluster Engine | last: Busby, B. | https://doi.org/10.64898/2026.11.18.767536
- biorxiv | Branched-Chain α-Keto Acid Mitochondrial Uptake Regulates Fatty Acid Metabolism in Adipose Tissue | last: Zhang, X. | https://doi.org/10.64898/2026.11.15.766772
- biorxiv | Fragment anchoring for metabolite annotation beyond whole-spectrum similarity | last: Lee, D. Y. | https://doi.org/10.64898/2026.11.11.766011
- biorxiv | Breadth over Depth: Predictor-Agnostic Consensus for Improved Antibody--Antigen Structure Prediction | last: Berger, B. | https://doi.org/10.64898/2026.11.17.767212
- biorxiv | Investigating the effect of acute consumption of kiwifruit on cognitive function using functional MRI | last: Francis, S. | https://doi.org/10.64898/2026.11.09.765279
- biorxiv | Predicting conformational changes induced by biomolecular interactions | last: Oh, B.-H. | https://doi.org/10.64898/2026.10.26.760299
- biorxiv | Semaglutide quiets "food noise" in mice by impairing the wanting, but not the liking, of glucose | last: Gutierrez, R. | https://doi.org/10.64898/2026.11.18.767696
- biorxiv | Tonic dopamine regulates cell-type-specific PKA activity and motivated behavior | last: Sabatini, B. L. | https://doi.org/10.64898/2026.11.18.767692
- biorxiv | Early life stress reduces prefrontal dendritic spine density in adult male mice | last: Alarcon, J. M. | https://doi.org/10.64898/2026.11.18.767676
- biorxiv | Dissociated network and cellular remodeling in the hippocampal-cortical circuit after induction of neuronal hyperexcitability | last: Llamosas, N. | https://doi.org/10.64898/2026.11.18.767525
- biorxiv | The mechanical nature of injury shapes the composition and temporal dynamics of inflammation after traumatic spinal cord injury | last: Nothias, F. | https://doi.org/10.64898/2026.11.18.767599
- biorxiv | Targeting Heparan Sulfate 3-O-Sulfation Enhances Acetylcholine Receptor Clustering and Stabilizes Neuromuscular Junctions in Duchenne Muscular Dystrophy | last: Stettler, O. | https://doi.org/10.64898/2026.11.18.767572
- biorxiv | Constructing value on the fly from episodic memory supports flexible decision-making | last: Pezzulo, G. | https://doi.org/10.64898/2026.11.18.767634
- biorxiv | Quantum-assisted genomic prediction of blast resistance in rice (Oryza sativa L.) using SNP and haplotype representations | last: SELVARAJ, M. G. | https://doi.org/10.64898/2026.11.18.767717
- biorxiv | Sparrowhawk: harnessing WebAssembly for private microbial genomics, and beyond | last: Lees, J. A. | https://doi.org/10.64898/2026.11.18.767565
- biorxiv | Machine Learning-Assisted Raman Spectroscopy for Quantitative Prediction of Multicomponent Mixtures | last: Wu, H.-J. | https://doi.org/10.64898/2026.11.18.767617
- biorxiv | Localizing Unsampled Regions in Partially Sampled Pathogen Phylogenies Using Machine Learning | last: RoyChoudhury, A. | https://doi.org/10.64898/2026.11.18.767590
- biorxiv | Prediction and Dissection of Nitrogenase Activity Based on Protein Sequences using Dual Descriptor | last: Ma, B.-G. | https://doi.org/10.64898/2026.11.18.767551
- biorxiv | Temporal blood sampling improves parameter recovery in a model of enterohepatic bile acid circulation using surrogate-accelerated Bayesian inference | last: de Buyl, S. | https://doi.org/10.64898/2026.11.18.766999
- biorxiv | NeuroImgAgent: a multi-agent platform for cross-species fMRI analysis with evidence-gated quality control | last: He, Y. | https://doi.org/10.64898/2026.11.19.767770
- biorxiv | Pharmacological co-targeting of Hippo and Wnt pathways induces robust Muller glia proliferation and reprogramming in the adult mouse retina | last: Liao, Y. | https://doi.org/10.64898/2026.11.18.767564
- biorxiv | Sensory Change Detection Unfolds Within a Shared Low-Dimensional Brain-State Landscape | last: Razavi, B. | https://doi.org/10.64898/2026.11.18.767177
- biorxiv | The information architecture of the naturalistic human brain | last: Mediano, P. A. M. | https://doi.org/10.64898/2026.11.18.767548
- biorxiv | fMRI hyperscanning reveals that coordinated exploration predicts successful conversation | last: Tamir, D. | https://doi.org/10.64898/2026.11.18.767620
- biorxiv | AAV-Mediated Astrogliosis Recapitulates Early Neuroinflammatory and Bioenergetic Features of Alzheimer''s Disease in Mice | last: Haris, M. | https://doi.org/10.64898/2026.11.18.767679
- biorxiv | Testing hypothesized neural substrates with lesions | last: Nachev, P. | https://doi.org/10.64898/2026.11.18.767704
- biorxiv | Historeceptomics Profiling of Ketamine | last: Cardozo, T. | https://doi.org/10.64898/2026.11.18.767642
- biorxiv | Temporal regularity shapes thalamocortical responses and deviance sensitivity in the anesthetized rat | last: Auksztulewicz, R. | https://doi.org/10.64898/2026.11.18.767747
- biorxiv | Adaptive behaviors emerge from Hebbian-like plasticity through flexible attractors | last: Erlich, J. C. | https://doi.org/10.64898/2026.11.18.767638
- biorxiv | B cell tolerance is dysregulated in people with complex regional pain syndrome: A high-dimensional immunophenotyping study | last: Austin, P. J. | https://doi.org/10.64898/2026.11.18.760656
- biorxiv | Filtration attenuates cannabis smoke-induced impacts on primary human airway epithelial cells | last: Hirota, J. A. | https://doi.org/10.64898/2026.11.18.767664
- biorxiv | IPF Patient Derived Lung Macrophages are Crucial In Signaling Fibroblast Activation and Disease Pathogenesis | last: Malik, A. | https://doi.org/10.64898/2026.11.18.767401
- biorxiv | A dynamic role for the apical extracellular matrix in cell migration during Drosophila abdominal morphogenesis | last: Bischoff, M. | https://doi.org/10.64898/2026.11.18.767616
- biorxiv | Mitochondria morphology changes dynamically during germ cell differentiation and under chemical stress in C. elegans: a quantitative ultrastructural study. | last: Mattout, A. | https://doi.org/10.64898/2026.11.18.767639
- biorxiv | AMBER: mapping accessible chromatin associations through barcode seed expansion | last: Zhu, C. | https://doi.org/10.64898/2026.11.18.767643
- biorxiv | Apples-to-apples transcriptomics: a parent-of-origin-resolved 'Granny Smith' genome reveals how reference choice shapes biological interpretation | last: Honaas, L. A. | https://doi.org/10.64898/2026.11.17.767359
- biorxiv | MitoArc: A Reproducible Short-Read Workflow for Human Mitochondrial Genome Analysis with Circular-Coordinate and NUMT-Aware Evaluation | last: Haldar, A. | https://doi.org/10.64898/2026.11.19.767817
- biorxiv | AIO Part I: Interpretable ADMET Prediction for Cyclic Peptides and Macrocycles | last: Qian, Y. | https://doi.org/10.64898/2026.11.18.767182
- biorxiv | Surrogate Verifiers Shape Decisions in Closed-Loop Experimental Design | last: Patz, M. | https://doi.org/10.64898/2026.11.18.767545
- biorxiv | Sex-dependent gating of astrocyte-driven nociceptive plasticity | last: Drdla-Schutting, R. | https://doi.org/10.64898/2026.11.18.767473
- biorxiv | Rage bait: a neurofunctional signature of moral outrage elicited by social media | last: Becker, B. | https://doi.org/10.64898/2026.11.18.767526
- biorxiv | Expanded representation and function of PDF neurons in the mosquito circadian network | last: Duvall, L. B. | https://doi.org/10.64898/2026.11.19.767825
- biorxiv | ER-vacuole tether Mdm1 coordinates lipid homeostasis to support autophagosome formation | last: Hariri, H. | https://doi.org/10.64898/2026.11.18.766846
- biorxiv | Proteome-scale inference of transcription factor binding motifs from predicted protein-DNA structures | last: Royer, L. A. | https://doi.org/10.64898/2026.11.18.767614
- biorxiv | Body-wide microbial ecosystem reorganization across the cognitive impairment spectrum in Parkinsons disease | last: Yildirim, S. | https://doi.org/10.64898/2026.11.17.767360
- biorxiv | Common organization of collective dynamics across divergent self-organized neural architectures | last: Levchenko, A. | https://doi.org/10.64898/2026.11.18.767733
- biorxiv | Preprocessing Determines Whether Fractal Biomarkers Detect Neurodegeneration: A Systematic Evaluation Across Five fMRI Pipelines | last: Thompson, P. | https://doi.org/10.64898/2026.11.06.763877
- biorxiv | Prolonged loss of D1 receptor signaling promotes maladaptive plasticity of direct pathway striatal projection neurons | last: Tritsch, N. X. | https://doi.org/10.64898/2026.11.18.767715
- biorxiv | ASTEROID, A Validated Annotated Dataset of Analytical Decisions in Graph Theory Based fMRI | last: Imam, S. H. | https://doi.org/10.64898/2026.11.06.764858
- biorxiv | Data-Driven Decomposition of Precisely Aligned Fiber-Orientation-Preserving Probabilistic Tractography Connectomes with Non-Negative Matrix Factorization | last: Glasser, M. F. | https://doi.org/10.64898/2026.11.08.765179
- biorxiv | Modelling vortex interactions reveals distinct patterns of brain reconfiguration following psilocybin and escitalopram | last: Deco, G. | https://doi.org/10.64898/2026.11.06.764626
- medrxiv | Complementary DNA-contact and domain-destabilizing mechanisms of PAX9 and MSX1 variants in non-syndromic tooth agenesis: an AlphaFold 3, ThermoMPNN, and AlphaGenome study | last: de Toledo, A. N. | https://doi.org/10.64898/2026.11.17.26368325
