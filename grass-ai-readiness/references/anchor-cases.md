# Anchor cases: 18 expert-curated reference assessments

These are the expert-curated reference assessments reported in the manuscript (Supplementary Table S5), for the evidence snapshot of **2026-07-08**. Use them for calibration: when rating a new use case, find the closest anchor and match your gate ratings to how it was scored, so a new assessment stays consistent with the framework. In **snapshot-reproduction mode**, do not alter these ratings — they are the fixed reference point. In **current-evidence reassessment mode**, you may re-rate against newer evidence, but you must preserve the original anchor below and report any change separately (see SKILL.md, Assessment mode).

Gate codes: DV = Direct grass validation, IT = Input transparency, BA = Benchmark adequacy, AR = Accessibility and reuse. Ratings: P = Pass, Pa = Partial, ND = Not demonstrated.

> Evidence-location granularity: S5 records the evidence *source per gate* (full-text vs abstract, repository/SRA availability) and the representative reference/DOI, but not page/table/figure coordinates. The `Evidence locations` field below therefore points to the representative reference and the recorded per-gate source; finer page/table anchors can be added by the authors where needed.

| UC | Family | Tool / study | DV | IT | BA | AR | Leakage | Tier |
|----|--------|--------------|----|----|----|----|---------|------|
| UC01 | Genomic prediction and G×E | GBLUP with genotype-by-environment interaction for ryegrass dry-matter yield | P | P | P | Pa | No | Tier 2 |
| UC02 | Environment-aware statistical ranking | Factor-analytic G×E models for perennial ryegrass cultivar dry-matter yield | P | P | Pa | ND | No | Tier 2 |
| UC03 | Genomic prediction in polyploid forage grass | Allele-dosage-aware genomic selection in Panicum maximum | P | P | Pa | P | No | Tier 2 |
| UC04 | Joint-learning genomic prediction | Feature-selection and joint classification/regression for polyploid grasses | P | P | Pa | Pa | Unclear | Tier 3 |
| UC05 | Genomic prediction with pangenome-derived variants | SNP- and SV-based genomic selection in pearl millet | P | P | Pa | Pa | No | Tier 2 |
| UC06 | Regional genomic prediction | G×E-aware genomic prediction with yield-surrogate traits in switchgrass | P | P | P | Pa | No | Tier 2 |
| UC07 | Genomic prediction and G×E | Genotype-by-environment predictive ability in Miscanthus | P | P | P | Pa | No | Tier 2 |
| UC08 | Genomic prediction and G×E | Reaction-norm and envirotyping GP at the limit of ryegrass distribution | P | P | P | Pa | No | Tier 2 |
| UC09 | Genome foundation-model benchmarking | Benchmark of general DNA foundation models | ND | P | ND | P | No | Tier 3 |
| UC10 | Pangenome and structural variation | Pearl millet graph pangenome and heat-tolerance SV interpretation | P | P | P | Pa | No | Tier 2 |
| UC11 | Pangenome and structural variation | Setaria graph genome, pangenome variation and multi-environment trait mapping | P | P | Pa | P | No | Tier 2 |
| UC12 | Single-cell and epigenomic interpretation | Pearl millet single-cell heat-stress atlas with WGCNA and functional follow-up | P | P | Pa | Pa | No | Tier 2 |
| UC13 | Single-cell and spatial transcriptomics | Phragmites single-cell/spatial atlas and B-chromosome association with invasiveness | P | P | Pa | P | No | Tier 2 |
| UC14 | Regulatory deep learning | Basenji-HMM cross-species chromatin-accessibility and cCRE prediction in grasses | P | P | P | P | No | Tier 2 |
| UC15 | Deep phenotyping | YOLOv8 tiller quantification in interspecific bentgrass hybrids | P | P | Pa | Pa | No | Tier 2 |
| UC16 | Deep phenotyping | Mask R-CNN stomatal density and area phenotyping in sorghum | P | P | P | Pa | No | Tier 2 |
| UC17 | Plant DNA foundation model | PlantCAD2 long-context DNA language model | Pa | P | Pa | Pa | Unclear | Tier 3 |
| UC18 | Cross-species sequence-to-expression benchmarking | Current genomic DL architectures across grass species and alleles | P | P | P | P | No | Tier 2 |

## Per-case detail

### UC01 — Tier 2 (Genomic prediction and G×E)
- **Tool / resource or study:** GBLUP with genotype-by-environment interaction for ryegrass dry-matter yield
- **Species / evidence domain:** Perennial ryegrass; 72 base cultivars; 23 multi-harvest, multi-site trials in south-eastern Australia
- **Stated task:** Estimate environment-specific seasonal and annual dry-matter yield and compare cultivar rankings across mega-environments
- **Intended user action:** Support cultivar and parent ranking within the represented Australian regional evaluation system — classified as *operational decision support*
- **Source citation:** Zhu et al. 2025, Frontiers in Plant Science 16:1579376
- **DOI / source URL:** https://doi.org/10.3389/fpls.2025.1579376
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + repository statement
- **Extracted evidence — Direct grass validation:** Direct target-grass evidence; regional multi-site/multi-harvest trials and environment-specific cultivar performance were evaluated.
- **Extracted evidence — Input transparency:** Trial structure, genomic relationships, spatial correction, G×E model and target mega-environments are reported; genotype allele-frequency data are publicly deposited.
- **Extracted evidence — Benchmark adequacy:** Leave-one-out validation and comparison against the industry-standard BLUE model directly assess the stated within-system ranking task.
- **Extracted evidence — Accessibility and reuse:** Genotype dataset is public, but analysis code and a complete executable environment were not clearly archived in the article.
- **Critical limitation:** Evidence is strongest within the represented regional trial system; large-scale real-world implementation was still identified as requiring further validation.
- **Why this tier:** All critical evidence gates are demonstrated, but reuse is partial; the rating is therefore capped below Tier 1 pending reproducible code/workflow access.
- **Use boundary:** Not evidence for transfer to new breeding cycles, families or production regions without renewed validation.
- **To advance:** Archive analysis code, software versions and a reusable workflow; add temporal or breeding-cycle-separated validation.

### UC02 — Tier 2 (Environment-aware statistical ranking)
- **Tool / resource or study:** Factor-analytic G×E models for perennial ryegrass cultivar dry-matter yield
- **Species / evidence domain:** Perennial ryegrass; 126 cultivars/breeding lines; 18 trials spanning 14 years in south-eastern Australia
- **Stated task:** Model multi-environment, multi-harvest dry-matter yield and identify mega-environment-specific cultivar rankings
- **Intended user action:** Provide environment-specific cultivar performance estimates for pasture evaluation — classified as *operational decision support*
- **Source citation:** Zhu et al. 2023, Field Crops Research 303:109143
- **DOI / source URL:** https://doi.org/10.1016/j.fcr.2023.109143
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=ND · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text
- **Extracted evidence — Direct grass validation:** Direct grass and regional use-case evidence from a long-running multi-environment trial network.
- **Extracted evidence — Input transparency:** Trials, harvests, spatial structure, model equations and covariance structures are described in detail.
- **Extracted evidence — Benchmark adequacy:** Models were compared by fit and used for prediction, but the study is not a marker-based GP deployment test and lacks a clearly independent held-out deployment evaluation.
- **Extracted evidence — Accessibility and reuse:** The underlying trial data cannot be shared because the authors do not have permission.
- **Critical limitation:** Data-access restrictions limit independent reproduction and re-analysis.
- **Why this tier:** Direct validation passes, but accessibility is not demonstrated and benchmark evidence is partial for prospective deployment.
- **Use boundary:** Supports regional cultivar evaluation, not genomic selection of untested germplasm.
- **To advance:** Provide a de-identified reproducible benchmark or synthetic/authorized validation set and executable scripts.

### UC03 — Tier 2 (Genomic prediction in polyploid forage grass)
- **Tool / resource or study:** Allele-dosage-aware genomic selection in Panicum maximum
- **Species / evidence domain:** Autotetraploid Panicum maximum; recurrent-selection population of 530 genotypes; six traits
- **Stated task:** Compare tetraploid versus diploid dosage representations and genomic prediction models
- **Intended user action:** Rank individuals within the evaluated recurrent-selection population — classified as *operational decision support*
- **Source citation:** de C. Lara et al. 2019, G3 9:2463–2475
- **DOI / source URL:** https://doi.org/10.1534/g3.118.200986
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + GitHub/SRA/Figshare
- **Extracted evidence — Direct grass validation:** Direct validation in the focal tropical forage grass and breeding population.
- **Extracted evidence — Input transparency:** Phenotypes, marker filtering, dosage coding, longitudinal models and prediction procedures are reported.
- **Extracted evidence — Benchmark adequacy:** Cross-validation evaluates within-population prediction, but does not provide cross-cycle, family-separated or external population validation.
- **Extracted evidence — Accessibility and reuse:** Phenotypic and molecular data, R code, SRA reads and supplementary files are publicly available.
- **Critical limitation:** Closely related recurrent-selection material and internal cross-validation may overstate transferability.
- **Why this tier:** Benchmark adequacy is partial for operational selection beyond the evaluated population, so the case remains hypothesis-/selection-guiding rather than broadly decision-ready.
- **Use boundary:** Not evidence for new cycles, unrelated germplasm or other ploidy structures.
- **To advance:** Add cross-cycle or family-separated validation and uncertainty reporting in a prospective breeding setting.

### UC04 — Tier 3 (Joint-learning genomic prediction)
- **Tool / resource or study:** Feature-selection and joint classification/regression for polyploid grasses
- **Species / evidence domain:** Urochloa decumbens, Megathyrsus maximus and sugarcane biparental populations
- **Stated task:** Predict quantitative traits and performance classes using joint learning and marker selection
- **Intended user action:** Prioritize individuals and reduced marker panels in complex polyploid breeding populations — classified as *operational decision support*
- **Source citation:** Aono et al. 2022, Scientific Reports 12:12499
- **DOI / source URL:** https://doi.org/10.1038/s41598-022-16417-7
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=Pa · Leakage=Unclear
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + SRA
- **Extracted evidence — Direct grass validation:** Direct tests include two forage grasses and sugarcane, with measured quantitative traits.
- **Extracted evidence — Input transparency:** Populations, genotyping, feature selection, models and evaluation procedures are described in the full text.
- **Extracted evidence — Benchmark adequacy:** Multiple prediction settings and baselines are reported, but external breeding-cycle validation is absent and feature-selection nesting should be rechecked for every split.
- **Extracted evidence — Accessibility and reuse:** Sequencing accessions are public; complete analysis code and a versioned executable workflow were not clearly archived.
- **Leakage note:** Unclear – nested feature-selection not confirmed in the published evaluation
- **Critical limitation:** Potential optimism if marker selection is not fully nested inside each validation fold; no prospective deployment test.
- **Why this tier:** Feature-selection nesting could not be confirmed from the published evaluation; unresolved-leakage status is therefore Unclear and, per the non-compensation rule, the case is capped at Tier 3 pending a leakage audit. Direct validation and accessibility also remain partial.
- **Use boundary:** Not evidence that the reduced marker panels generalize across unrelated breeding populations.
- **To advance:** Verify feature-selection nesting; archive code; add external population or breeding-cycle validation.

### UC05 — Tier 2 (Genomic prediction with pangenome-derived variants)
- **Tool / resource or study:** SNP- and SV-based genomic selection in pearl millet
- **Species / evidence domain:** Pearl millet PMiGAP; 242 phenotyped accessions; 120 traits across control and drought conditions
- **Stated task:** Compare nine prediction models using SNPs versus structural variants and nominate high-GEBV accessions
- **Intended user action:** Prioritize candidate pearl millet accessions for follow-up breeding tests — classified as *operational decision support*
- **Source citation:** Yan et al. 2024, Theoretical and Applied Genetics 137:244
- **DOI / source URL:** https://doi.org/10.1007/s00122-024-04754-2
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + cited public datasets
- **Extracted evidence — Direct grass validation:** Direct pearl millet prediction using focal-species SNPs, pangenome-derived SVs and agronomic phenotypes.
- **Extracted evidence — Input transparency:** Reference accession, marker counts, phenotype filtering, models and 70/30 repeated cross-validation are reported.
- **Extracted evidence — Benchmark adequacy:** Random 70/30 splits were repeated, but phenotypes had single replication and no family-, environment- or cycle-separated external test was performed.
- **Extracted evidence — Accessibility and reuse:** Input datasets derive from public studies, but a complete code/workflow archive for this analysis was not confirmed.
- **Critical limitation:** Random cross-validation and single-replicate phenotypes limit evidence for operational selection.
- **Why this tier:** Direct validation passes, but benchmark adequacy and reproducible reuse are partial.
- **Use boundary:** Candidate GEBVs are not proof of realized breeding gain or cross-environment stability.
- **To advance:** Validate candidates prospectively with replicated trials; use family/cycle/environment-separated splits and archive code.

### UC06 — Tier 2 (Regional genomic prediction)
- **Tool / resource or study:** G×E-aware genomic prediction with yield-surrogate traits in switchgrass
- **Species / evidence domain:** Switchgrass diversity panel evaluated across multiple regional field environments
- **Stated task:** Predict regional biomass performance while accounting for G×E and limited target-site observations
- **Intended user action:** Rank switchgrass candidates for a represented region when matched multi-site training and at least one target-relevant observation/surrogate are available — classified as *operational decision support*
- **Source citation:** Tilhou et al. 2024, G3 14:jkae159
- **DOI / source URL:** https://doi.org/10.1093/g3journal/jkae159
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + accessible SRA; cited Dryad repository unresolved at snapshot
- **Extracted evidence — Direct grass validation:** Direct switchgrass, multi-environment and breeding-facing evidence.
- **Extracted evidence — Input transparency:** Genotypes, environments, traits, relationship models and prediction scenarios are documented.
- **Extracted evidence — Benchmark adequacy:** Validation scenarios explicitly test unobserved individuals/sites and compare genetic-only, G×E and surrogate-trait information under the stated regional use.
- **Extracted evidence — Accessibility and reuse:** Sequencing data are accessible through SRA (BioProject PRJNA622568; study SRP258586), but the cited Dryad repository containing the realized relationship matrix, mean field performance, SNP subset and example code did not resolve when checked on 8 July 2026. Accessibility and reuse are therefore rated Partial.
- **Critical limitation:** Performance is use-condition dependent; genetic-only prediction in a genuinely novel region can be weak.
- **Why this tier:** Direct switchgrass validation, transparent study inputs and a claim-matched regional genotype-by-environment benchmark support hypothesis-guiding use within the represented regional setting. However, incomplete access to the analysis-ready field-performance data, relationship matrix, SNP subset and example code prevents a Tier 1 designation under the non-compensation rule.
- **Use boundary:** Decision-ready only under the specified matched regional-data condition.
- **To advance:** Restore or replace the repository link and provide persistent access to the analysis-ready field-performance data, realized relationship matrix, SNP subset, preprocessing information and executable example code before reconsidering Tier 1.

### UC07 — Tier 2 (Genomic prediction and G×E)
- **Tool / resource or study:** Genotype-by-environment predictive ability in Miscanthus
- **Species / evidence domain:** Miscanthus sinensis and M. sacchariflorus panels across Northern Hemisphere trial locations
- **Stated task:** Assess whether multi-location GS models predict biomass yield in untested environments
- **Intended user action:** Guide parent prioritization and identify where additional target-environment trials are needed — classified as *operational decision support*
- **Source citation:** Widener et al. 2024, GCB Bioenergy 16:e13113
- **DOI / source URL:** https://doi.org/10.1111/gcbb.13113
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + data repositories
- **Extracted evidence — Direct grass validation:** Direct Miscanthus evidence across multiple species panels and environments.
- **Extracted evidence — Input transparency:** Reference versions, SNP filtering, trial locations/years, environmental variables and models are documented.
- **Extracted evidence — Benchmark adequacy:** The evaluation explicitly targets untested environments and exposes latitude-dependent failure boundaries.
- **Extracted evidence — Accessibility and reuse:** Phenotypic/environmental data are openly deposited, but analysis code was not clearly archived.
- **Critical limitation:** Prediction was poorer at higher latitudes, reflecting sparse or mismatched target-environment representation.
- **Why this tier:** Validation is strong, but practical reuse is partial and the study itself identifies target-environment coverage gaps.
- **Use boundary:** Not decision-ready for high-latitude environments absent representative training trials.
- **To advance:** Release analysis code; increase high-latitude trials; add calibrated uncertainty for target-environment predictions.

### UC08 — Tier 2 (Genomic prediction and G×E)
- **Tool / resource or study:** Reaction-norm and envirotyping GP at the limit of ryegrass distribution
- **Species / evidence domain:** Perennial ryegrass; 264 diverse accessions across six Nordic/Baltic countries
- **Stated task:** Predict yield, spring cover and winter kill in unobserved countries and genetically distinct germplasm
- **Intended user action:** Support adaptation-oriented candidate ranking while identifying extrapolation failures — classified as *operational decision support*
- **Source citation:** Johansen et al. 2025, Theoretical and Applied Genetics 138:281
- **DOI / source URL:** https://doi.org/10.1007/s00122-025-05064-x
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + Zenodo data record + public GitHub analysis repository
- **Extracted evidence — Direct grass validation:** Direct ryegrass GP across contrasting environments and diverse germplasm.
- **Extracted evidence — Input transparency:** Genotyping, environmental covariates, reaction-norm/envirotyping models and trait definitions are reported.
- **Extracted evidence — Benchmark adequacy:** Three claim-matched validation schemes include leave-one-country-out and leave-one-genetic-cluster-out, with explicit failure analysis.
- **Extracted evidence — Accessibility and reuse:** Data and analysis scripts are publicly available through a persistent Zenodo record and a public GitHub repository. The deposited files include raw SNP data, processed genomic and environmental matrices, raw and processed phenotypes, environmental data and analysis scripts. However, the code repository lacks an explicit software licence, detailed stepwise execution instructions and a pinned computational environment, and some scripts contain local absolute paths. Accessibility and reuse is therefore rated Partial.
- **Critical limitation:** Prediction for genetically novel clusters was highly variable and could be near zero or negative.
- **Why this tier:** Direct perennial ryegrass validation, transparent inputs and claim-matched country- and genetic-cluster-based validation support strong hypothesis-guiding use. However, reuse remains partial because the public code package lacks an explicit licence, a pinned computational environment and sufficiently portable stepwise execution documentation. Performance also declined markedly for genetically distant germplasm, preventing broad decision-ready claims.
- **Use boundary:** Not reliable for genetically distant germplasm without revalidation.
- **To advance:** Add an explicit software licence; archive a versioned code release with a persistent DOI; replace local absolute paths with relative or configurable paths; report package and software versions; provide stepwise execution instructions; and add prospective breeding-cycle validation and calibrated uncertainty thresholds before reconsidering Tier 1.

### UC09 — Tier 3 (Genome foundation-model benchmarking)
- **Tool / resource or study:** Benchmark of general DNA foundation models
- **Species / evidence domain:** Primarily human/general genomic benchmark domains; no direct grass decision endpoint
- **Stated task:** Compare zero-shot DNA foundation-model embeddings across sequence, expression, variant and genome-structure tasks
- **Intended user action:** Use general-DNA model rankings to prioritize functional variants or breeding candidates in a grass species — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Feng et al. 2025, Nature Communications 16:10780
- **DOI / source URL:** https://doi.org/10.1038/s41467-025-65823-8
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=ND · IT=P · BA=ND · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + Hugging Face/GitHub/Zenodo
- **Extracted evidence — Direct grass validation:** The study benchmarks general genomic tasks but does not validate a focal grass species, breeding population or grass decision endpoint.
- **Extracted evidence — Input transparency:** Models, checkpoints, tasks, preprocessing and benchmark datasets are described.
- **Extracted evidence — Benchmark adequacy:** The benchmark is rigorous for its published general tasks, but it is not task-matched to grass variant prioritization or breeding decisions.
- **Extracted evidence — Accessibility and reuse:** Processed datasets, code, MIT licence and a versioned Zenodo archive are available.
- **Critical limitation:** Strong general benchmarking does not establish biological validity in grasses.
- **Why this tier:** Direct validation and task-matched benchmark adequacy are both ND for the stated grass decision use; the non-compensation rule therefore fixes Tier 3.
- **Use boundary:** May serve as a baseline or benchmark-design resource, not as evidence for grass decisions.
- **To advance:** Add held-out grass species/populations, grass-specific endpoints, simpler baselines, calibration and allele-level failure analysis.

### UC10 — Tier 2 (Pangenome and structural variation)
- **Tool / resource or study:** Pearl millet graph pangenome and heat-tolerance SV interpretation
- **Species / evidence domain:** Pearl millet; 10 newly assembled + 1 existing chromosome-scale assemblies (11 total), population resequencing, transcriptomics and functional assays
- **Stated task:** Identify SVs and regulatory mechanisms associated with heat tolerance
- **Intended user action:** Prioritize heat-tolerance SVs, genes and mechanisms for experimental follow-up — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Yan et al. 2023, Nature Genetics 55:507–518
- **DOI / source URL:** https://doi.org/10.1038/s41588-023-01302-4
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + public repositories
- **Extracted evidence — Direct grass validation:** Direct focal-grass evidence includes SV–expression relationships and experimental validation of an RWP-RK heat-response regulator.
- **Extracted evidence — Input transparency:** Assembly inputs, graph construction, SV classes, population data and multi-omics procedures are extensively documented.
- **Extracted evidence — Benchmark adequacy:** Assembly/SV quality was evaluated with multiple metrics, callers, PCR/read support and orthogonal biological assays for the mechanism-guiding use.
- **Extracted evidence — Accessibility and reuse:** Raw data and assemblies are public; the study used published tools, but no complete end-to-end custom workflow archive was identified.
- **Critical limitation:** Validated mechanisms do not make every predicted SV causal or breeding-decision ready.
- **Why this tier:** Four-gate evidence is strong, but the intended action is candidate/mechanism prioritization rather than an operational breeding decision, and reuse is partial.
- **Use boundary:** Trait-linked SVs require validation in target breeding pools and environments.
- **To advance:** Provide reusable graph/variant workflow and prospective target-pool validation of selected SVs.

### UC11 — Tier 2 (Pangenome and structural variation)
- **Tool / resource or study:** Setaria graph genome, pangenome variation and multi-environment trait mapping
- **Species / evidence domain:** Setaria italica/S. viridis; 110 assemblies, 1,844 accessions, 68 traits across 13 environments
- **Stated task:** Construct a graph genome, identify SVs and map trait-associated variation
- **Intended user action:** Build reference-bias-aware features and prioritize trait-linked genes/SVs — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** He et al. 2023, Nature Genetics 55:1232–1242
- **DOI / source URL:** https://doi.org/10.1038/s41588-023-01423-w
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + NCBI/Zenodo/GitHub
- **Extracted evidence — Direct grass validation:** Direct Setaria evidence with focal-species graph construction, trait mapping and multi-environment phenotypes.
- **Extracted evidence — Input transparency:** Assemblies, quality metrics, variant procedures, populations, traits and downstream analyses are described.
- **Extracted evidence — Benchmark adequacy:** Graph and variant quality are extensively checked, but breeding-potential predictions use repeated random splits rather than external cycles or populations.
- **Extracted evidence — Accessibility and reuse:** Assemblies, phenotypes, code and source data are publicly deposited in NCBI, Zenodo and GitHub.
- **Critical limitation:** Random validation does not prove transfer to new breeding cycles or production populations.
- **Why this tier:** Benchmark adequacy is partial for decision use; the resource is highly reusable but remains hypothesis-/feature-construction ready.
- **Use boundary:** Trait associations and simulated breeding potential are not realized genetic gain.
- **To advance:** Add pangenome-aware external prediction and prospective selection validation.

### UC12 — Tier 2 (Single-cell and epigenomic interpretation)
- **Tool / resource or study:** Pearl millet single-cell heat-stress atlas with WGCNA and functional follow-up
- **Species / evidence domain:** Pearl millet Tifleaf_3 leaves under control, heat, priming and triggering conditions
- **Stated task:** Resolve cell-type-specific heat-stress memory and prioritize UGT73C3-related mechanisms
- **Intended user action:** Guide mechanistic experiments and candidate-gene prioritization for heat tolerance — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Jin et al. 2025, New Phytologist 247:637–650
- **DOI / source URL:** https://doi.org/10.1111/nph.70232
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text
- **Extracted evidence — Direct grass validation:** Direct pearl millet single-cell evidence with cell-type-resolved stress responses and functional follow-up.
- **Extracted evidence — Input transparency:** Plant material, stress design, replicates, reference genome, filtering thresholds, software versions and orthogonal assays are reported.
- **Extracted evidence — Benchmark adequacy:** Single-cell findings are cross-checked with bulk RNA-seq, CUT&Tag and rice mutant/overexpression assays, but causal validation is not in pearl millet and population transfer is untested.
- **Extracted evidence — Accessibility and reuse:** Data deposition is expected/reported in the article package, but a complete reusable analysis-code archive was not confirmed in this assessment.
- **Critical limitation:** Functional validation in rice does not fully establish the same causal effect in pearl millet populations.
- **Why this tier:** The case supports mechanism-guiding use; benchmark and reuse are partial for stronger biological or breeding decisions.
- **Use boundary:** Not population-level evidence for heat-tolerance selection.
- **To advance:** Validate in pearl millet; release code/processed objects; test across genotypes, stages and field heat regimes.

### UC13 — Tier 2 (Single-cell and spatial transcriptomics)
- **Tool / resource or study:** Phragmites single-cell/spatial atlas and B-chromosome association with invasiveness
- **Species / evidence domain:** Phragmites australis; European non-invasive and North American invasive populations
- **Stated task:** Map cell states spatially and identify B-chromosome-enriched, population-associated expression programs
- **Intended user action:** Generate cell-type-specific hypotheses about invasiveness and regenerative growth — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Wang et al. 2026, Genome Biology 27:184
- **DOI / source URL:** https://doi.org/10.1186/s13059-026-04079-x
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + SRA/GitHub/Zenodo
- **Extracted evidence — Direct grass validation:** Direct evidence in a non-model wetland grass, using single-cell and spatial data from native/invasive population contrasts.
- **Extracted evidence — Input transparency:** Sampling, common-garden design, scRNA-seq/spatial workflows, annotations and comparison procedures are reported.
- **Extracted evidence — Benchmark adequacy:** Spatial projection, pseudobulk and sensitivity analyses support interpretation, but the biological sample count is small and B-chromosome associations are not causal tests.
- **Extracted evidence — Accessibility and reuse:** Raw data, analysis scripts and archived materials are linked through SRA, GitHub and Zenodo.
- **Critical limitation:** Population association and B-chromosome enrichment do not prove causation of invasiveness.
- **Why this tier:** Strong direct and reusable evidence supports mechanistic hypothesis generation, not management or breeding decisions.
- **Use boundary:** Not a causal intervention test and not representative of all Phragmites populations.
- **To advance:** Expand population replication and experimentally manipulate/segregate B chromosomes or prioritized pathways.

### UC14 — Tier 2 (Regulatory deep learning)
- **Tool / resource or study:** Basenji-HMM cross-species chromatin-accessibility and cCRE prediction in grasses
- **Species / evidence domain:** Five Poaceae species and five orthologous tissues
- **Stated task:** Learn sequence-to-accessibility rules, transfer across grasses and delineate candidate CREs
- **Intended user action:** Prioritize grass regulatory elements and cross-species regulatory hypotheses — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Li et al. 2026, Molecular Plant, doi:10.1016/j.molp.2026.05.017
- **DOI / source URL:** https://doi.org/10.1016/j.molp.2026.05.017
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text + SRA/NGDC/GitHub
- **Extracted evidence — Direct grass validation:** Direct multi-grass evidence, including within- and cross-species predictions against observed ATAC-seq.
- **Extracted evidence — Input transparency:** Genome assemblies, tissues, non-overlapping train/validation/test windows, model configuration and evaluation metrics are documented.
- **Extracted evidence — Benchmark adequacy:** Within-species and cross-species tests, AUROC/AUPRC/PCC, model-version comparison and a distant Arabidopsis transfer baseline support the stated regulatory-prioritization task.
- **Extracted evidence — Accessibility and reuse:** Raw ATAC/RNA data, trained models, scripts and genome-wide element annotations are public.
- **Critical limitation:** Predicted cCREs and mutational effects remain candidates until locus-specific functional validation.
- **Why this tier:** All four gates pass, but the stated user action is hypothesis-guiding regulatory prioritization rather than an operational breeding or trait decision-support action; per the Rubric, such uses are capped at Tier 2 even when all gates pass.
- **Use boundary:** Not evidence that a predicted element changes an agronomic trait in a target population.
- **To advance:** Add allele-level perturbation, target-population context and trait-linked validation.

### UC15 — Tier 2 (Deep phenotyping)
- **Tool / resource or study:** YOLOv8 tiller quantification in interspecific bentgrass hybrids
- **Species / evidence domain:** Interspecific bentgrass hybrids under a controlled image-acquisition workflow
- **Stated task:** Automate tiller counting under dense overlap and compare computer-vision models
- **Intended user action:** Generate scalable tiller-count phenotypes for the evaluated imaging conditions — classified as *operational decision support*
- **Source citation:** Ferm et al. 2026, Frontiers in Plant Science 17:1810220
- **DOI / source URL:** https://doi.org/10.3389/fpls.2026.1810220
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=Pa · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text
- **Extracted evidence — Direct grass validation:** Direct turfgrass evidence with manual/reference counts and hybrid plant material.
- **Extracted evidence — Input transparency:** Plant material, imaging, annotations, model settings and group-size evaluation are reported.
- **Extracted evidence — Benchmark adequacy:** YOLOv8 is compared with OpenCV and Faster R-CNN and tested across density regimes, but no independent camera/site/species dataset establishes external transfer.
- **Extracted evidence — Accessibility and reuse:** The article and supplement contain the reported contributions, but no open image/code/model repository is specified.
- **Critical limitation:** The workflow is intentionally narrow and does not demonstrate field, camera or species transfer.
- **Why this tier:** Direct validation passes, but benchmark and reuse are partial; the use remains validated trait extraction under restricted conditions.
- **Use boundary:** Not decision-ready outside the described imaging and plant-density regime.
- **To advance:** Release images/annotations/code/weights and validate on independent imaging systems, seasons and grass species.

### UC16 — Tier 2 (Deep phenotyping)
- **Tool / resource or study:** Mask R-CNN stomatal density and area phenotyping in sorghum
- **Species / evidence domain:** Sorghum association panel; 311 accessions; two field environments
- **Stated task:** Automate stomatal segmentation/counting and compare with manual phenotyping for GWAS-ready traits
- **Intended user action:** Extract stomatal density and complex-area phenotypes under the reported microscopy workflow — classified as *operational decision support*
- **Source citation:** Bheemanahalli et al. 2021, Plant Physiology 186:1562–1579
- **DOI / source URL:** https://doi.org/10.1093/plphys/kiab174
- **Source version:** Version of record
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=Pa · Leakage=No
- **Evidence locations (per gate source):** DV=full-text; IT=full-text; BA=full-text; AR=full-text
- **Extracted evidence — Direct grass validation:** Direct sorghum evidence across two field environments, with manual measurements, GWAS concordance and physiological follow-up.
- **Extracted evidence — Input transparency:** Training/validation image counts, model architecture, field environments, trait definitions and downstream analyses are described.
- **Extracted evidence — Benchmark adequacy:** Manual-versus-model agreement, independent image evaluation, two environments and downstream genetic/physiological concordance support the narrow trait-extraction task.
- **Extracted evidence — Accessibility and reuse:** Article and supplements are available, but reusable code, weights and the full annotated image set were not clearly archived.
- **Critical limitation:** External transfer to other microscopes, tissues, stages or species is not established.
- **Why this tier:** Biological and benchmark evidence pass, but accessibility is partial; Tier 1 is therefore not assigned.
- **Use boundary:** Decision-ready only for the reported phenotyping protocol after local calibration.
- **To advance:** Release code/weights/images and add independent cross-laboratory or cross-protocol validation.

### UC17 — Tier 3 (Plant DNA foundation model)
- **Tool / resource or study:** PlantCAD2 long-context DNA language model
- **Species / evidence domain:** Pretrained on 65 angiosperm genomes; plant cross-species functional-annotation benchmarks
- **Stated task:** Generate long-context plant sequence representations and transfer them across species/tasks
- **Intended user action:** Prioritize functional regions or candidate annotations in an under-resourced grass before experimental testing — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Zhai et al. 2025, bioRxiv 2025.08.27.672609, version 4
- **DOI / source URL:** https://doi.org/10.1101/2025.08.27.672609
- **Source version:** bioRxiv preprint; version 4 cited and confirmed on 2026-07-07; title revised in version 4
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=Pa · IT=P · BA=Pa · AR=Pa · Leakage=Unclear
- **Evidence locations (per gate source):** DV=full-text preprint; IT=full-text preprint; BA=full-text preprint; AR=preprint + GitHub
- **Extracted evidence — Direct grass validation:** Plant-specific and cross-species benchmarks include angiosperm evidence, but direct validation for the user's focal grass, population and decision is incomplete.
- **Extracted evidence — Input transparency:** Pretraining corpus, long-context architecture, public tasks and evaluation design are described in the preprint.
- **Extracted evidence — Benchmark adequacy:** Cross-species public benchmarks are substantial, but preprint versioning, potential overlap between pretraining and benchmarks, grass-specific held-out tests and allele-level failures require final checking.
- **Extracted evidence — Accessibility and reuse:** A public project repository exists, but exact model-weight, licence, checkpoint and reproducible-environment status should be reconfirmed for the submission snapshot.
- **Leakage note:** Unclear – pretraining/benchmark overlap for the plant DNA language model not audited at snapshot date
- **Critical limitation:** Preprint versions and repositories can change; plant-level transfer is not the same as focal-grass decision validation.
- **Why this tier:** Direct validation and benchmark adequacy are partial, and pretraining/benchmark overlap could not be audited from the preprint; unresolved-leakage status is therefore Unclear and the case is capped at Tier 3 pending version freeze, weights/licence confirmation and split-overlap audit.
- **Use boundary:** Not evidence for direct breeding or causal variant decisions.
- **To advance:** Freeze the cited version; verify weights/licence; use held-out grass lineages, pangenome/allelic sequences, calibration and simpler baselines.

### UC18 — Tier 2 (Cross-species sequence-to-expression benchmarking)
- **Tool / resource or study:** Current genomic DL architectures across grass species and alleles
- **Species / evidence domain:** Eighteen Andropogoneae grass species in total, including 15 training species, two validation species and maize as the held-out species; 26 maize lines were used for within-species allele evaluation
- **Stated task:** Test whether sequence-to-expression architectures generalize across species and within-species alleles
- **Intended user action:** Design realistic grass transfer benchmarks and set failure boundaries for sequence-to-expression models — classified as *hypothesis / mechanism / benchmark*
- **Source citation:** Wrightsman et al. 2024, bioRxiv 2024.04.11.589024
- **DOI / source URL:** https://doi.org/10.1101/2024.04.11.589024
- **Source version:** bioRxiv preprint; version 2 posted 2024-09-04 and confirmed as the cited version on 2026-07-07
- **Full text checked:** Yes
- **Evidence snapshot date:** 2026-07-08
- **Gates:** DV=P · IT=P · BA=P · AR=P · Leakage=No
- **Evidence locations (per gate source):** DV=full-text preprint; IT=full-text preprint; BA=full-text preprint; AR=full-text + Zenodo
- **Extracted evidence — Direct grass validation:** Direct multi-grass evidence explicitly evaluates species transfer and allele-level prediction.
- **Extracted evidence — Input transparency:** Species, orthogroup-aware splits, input windows, architectures, targets and metrics are described.
- **Extracted evidence — Benchmark adequacy:** The study directly contrasts held-out species and within-species allele tasks, compares four architectures and reports a clear failure boundary.
- **Extracted evidence — Accessibility and reuse:** The preprint and a versioned Zenodo research record are openly available.
- **Critical limitation:** Preprint status and evolving versions require snapshot citation; strong species transfer did not imply allele-level accuracy.
- **Why this tier:** All four gates pass for benchmark design and failure-boundary definition, but the stated user action is methodological (cross-species transfer-benchmark construction) rather than an operational biological or breeding decision; per the Rubric, such uses are capped at Tier 2.
- **Use boundary:** Not a decision-support model for allele ranking despite strong cross-species performance.
- **To advance:** Freeze the exact preprint/data version; independently replicate allele-level tests and add calibration/variant-aware inputs.
