[English](README.md) | [简体中文](README_zh-CN.md)

# Grass AI-genomics readiness framework — executable companion

[![tests](https://github.com/ashelylinluo/grass-ai-readiness/actions/workflows/test.yml/badge.svg)](https://github.com/ashelylinluo/grass-ai-readiness/actions/workflows/test.yml)

This repository accompanies the manuscript *"AI-driven grass genomics: an evidence-guided roadmap from bioinformatics resources to breeding decisions"* (Luo L, Sun Z, Lin Z, et al.). It provides an executable implementation of the readiness framework so that readers can inspect the manuscript-reported reference assessments and apply the same rubric to new use cases.

The framework asks a single question about any AI or bioinformatics result in grass/Poaceae genomics: **can it support a decision, only guide a hypothesis, or does it still need benchmarking?** A tool is not ready because it scores well — it is ready only when the evidence holds for the exact species, task, and user action claimed. Readiness is assigned as a use-case-specific **tier**:

- **Tier 1 — decision-support ready:** supports the specified action under the validated conditions (bounded, not a general endorsement).
- **Tier 2 — hypothesis-guiding:** supports prioritization, interpretation, or experimental design within the stated boundary.
- **Tier 3 — benchmark-required:** technically promising, but stronger task-specific validation is required first.

The tier is *derived from ordered decision rules applied to four evidence gates* — Direct grass validation, Input transparency, Benchmark adequacy, and Accessibility and reuse — never an average or an overall quality score. In the current evidence snapshot (2026-07-08), the 18 reference use cases are **0 Tier 1 / 15 Tier 2 / 3 Tier 3**.

---

## Quick reproducibility check

Clone the repository:

```bash
git clone https://github.com/ashelylinluo/grass-ai-readiness.git
cd grass-ai-readiness
```

Compile the Python scripts:

```bash
python -m compileall grass-ai-readiness/scripts
```

Reproduce the 18 reference assessments and 10 synthetic boundary tests:

```bash
python grass-ai-readiness/scripts/assign_tier.py \
  --selftest \
  grass-ai-readiness/references/anchor-cases.tsv \
  grass-ai-readiness/references/synthetic-boundary-tests.tsv
```

Expected output:

```text
28/28 rows reproduce — all consistent.
```

---

## What's here

Three artifacts, in increasing order of automation:

### 1. The rubric — `Supplementary_Table_S5.xlsx`
The definitions themselves: the four gate criteria (Pass / Partial / Not demonstrated), the leakage and action-type rules, the ordered decision rules, and the 18 expert-curated reference assessments (UC01–UC18) with their per-gate evidence. This is the source of truth; the other two artifacts operationalize it.

### 2. Interactive assessor — `grass-ai-readiness-assessor.html`
After GitHub Pages is enabled for this repository, open the interactive assessor at <https://ashelylinluo.github.io/grass-ai-readiness/grass-ai-readiness-assessor.html>.

A single self-contained web page (no server, no dependencies — open it in any browser). Set the four gate ratings, the leakage status, and the action type; the tier updates live and highlights **which decision rule fired**. Includes all 18 reference cases with per-gate evidence summaries and source details (citation, DOI, version, snapshot date) so each case is traceable back to its origin, browsable and filterable by tier. Best for humans who want to see the logic and inspect the reference cases.

### 3. Agent skill — `grass-ai-readiness/`
An [Agent Skill](https://agentskills.io/specification) that lets an AI assistant apply the rubric to **new** use cases, not just reproduce the 18. The assistant reads the evidence and rates the four gates; once the gate ratings, leakage status, and action type are fixed, a deterministic script assigns the tier using ordered rules. Best for assessing a tool the manuscript did not cover.

```
grass-ai-readiness/
├── SKILL.md                          # instructions the assistant follows
├── scripts/
│   ├── assign_tier.py                # deterministic tier assignment (the rules, in code)
│   └── validate_assessment.py        # checks an assessment is evidence-backed and rule-consistent
├── assets/
│   └── assessment-template.json      # fillable structured-output template
└── references/
    ├── rubric-definitions.md         # gate definitions + ordered decision rules
    ├── anchor-cases.md               # 18 reference assessments, with evidence + sources
    ├── anchor-cases.tsv              # machine-checkable form
    ├── synthetic-boundary-tests.md   # constructed rows exercising every rule (NOT literature cases)
    └── synthetic-boundary-tests.tsv  # machine-checkable form
```

A packaged `grass-ai-readiness.skill` file is also provided for one-click import into clients that support it. The open specification defines the *directory* containing `SKILL.md` as the portable format, so the folder above is the canonical distribution; the `.skill` file is a convenience only.

---

## Using each artifact

### The interactive assessor
After GitHub Pages is enabled, open the hosted assessor at <https://ashelylinluo.github.io/grass-ai-readiness/grass-ai-readiness-assessor.html>, or download `grass-ai-readiness-assessor.html` and open it in a browser. Nothing to install.

### The tier engine, directly
The decision rules run as a standalone script — useful for scripting or verification:

```bash
python grass-ai-readiness/scripts/assign_tier.py \
  --dv P --it P --ba P --ar Pa \
  --leakage No --action decision
# → Tier 2 — hypothesis-guiding   (Rule 7)
```

Reproduce every reference row (the 18 cases plus the synthetic boundary tests):

```bash
cd grass-ai-readiness
python scripts/assign_tier.py --selftest \
  references/anchor-cases.tsv references/synthetic-boundary-tests.tsv
# → 28/28 rows reproduce — all consistent.
```

Check that a completed assessment is auditable and rule-consistent:

```bash
python scripts/validate_assessment.py my_assessment.json
python scripts/validate_assessment.py --references references/
```

`validate_assessment.py` enforces that every gate carries extracted evidence *and* an evidence location, and that the recorded tier equals what the rules produce — a human-written tier cannot silently disagree with the engine.

### The agent skill
Install the `.skill` file (or point your agent at the `grass-ai-readiness/` directory), then ask a readiness question in natural language, e.g. *"Is a wheat-trained sequence-to-function model ready for ranking drought-linked regulatory variants in tall fescue?"* The assistant will establish the bounded use case, rate the four gates against the rubric with cited evidence, run `assign_tier.py`, and return an auditable assessment.

---

## Two assessment modes

Because repositories and preprints move, the skill distinguishes:

- **Snapshot reproduction** — reproduce the manuscript assessment as of 2026-07-08; the 18 anchor ratings are fixed.
- **Current-evidence reassessment** — recheck the current paper, repository, licence, and release, and re-rate on current evidence, preserving the original anchor and reporting any change separately with the recheck date.

Tiers are snapshots. A tier can move as evidence, code, or benchmarks change; recheck before relying on a rating.

---

## Scope and caveats

- Ratings are **use-case-specific** and are not rankings of papers, tools, developers, or overall scientific quality. Tier 3 is not a bad paper — it means the evidence for *that decision* is not yet in place.
- The tier travels with the stated species/task/action, not with the method. The same model can be Tier 1 in one validated population and Tier 3 after transfer.
- The 18 reference assessments are **expert-curated**, not independently re-validated.
- Assessments produced here are interpretive aids, not authoritative endorsements.
- The rubric is calibrated for grass/Poaceae AI-genomics; for use cases far outside that domain, the calibration may not transfer.

---

## Licence

Code and the interactive assessor are released under the MIT License (see `LICENSE`). Reference assessments, rubric text, and tabular data are released under CC BY 4.0 (see `LICENSE-DATA`).

## Citation

If you use this framework or its implementation, please cite the archived record (see also `CITATION.cff`):

> Luo L, Sun Z, Lin Z, et al. Supplementary data and literature-mapping records for "AI-driven grass genomics: a user-centric and evidence-guided roadmap from bioinformatics resources to breeding decisions". Zenodo, 2026. doi:10.5281/zenodo.20825481

*The title in the data-record citation above follows the current Zenodo metadata for that DOI; the manuscript title used at the top of this README reflects the current manuscript title.*

*The DOI above points to the existing data record. A separate software DOI for this executable companion will be minted when the GitHub release is archived to Zenodo; update the DOI here, in the HTML, and in `CITATION.cff` at that point.*

---

## Availability

The literature-mapping records and supplementary assessment data supporting the review are archived on Zenodo at https://doi.org/10.5281/zenodo.20825481.

The executable companion to the readiness framework is publicly available in this repository. It includes:

* the manuscript-defined four-gate rubric;
* 18 expert-curated reference use-case assessments;
* a browser-based interactive assessor;
* deterministic tier-assignment scripts;
* synthetic boundary tests covering all decision-rule paths; and
* an Agent Skill for evaluating new use cases.
