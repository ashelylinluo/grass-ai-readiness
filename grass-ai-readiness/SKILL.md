---
name: grass-ai-readiness
description: Assess whether an AI or bioinformatics tool in grass/Poaceae genomics is ready to support a decision, guide a hypothesis, or still needs benchmarking. Applies a four-gate rubric (direct grass validation, input transparency, benchmark adequacy, accessibility and reuse) and fixed decision rules to assign a use-case-specific readiness tier (Tier 1 decision-support ready, Tier 2 hypothesis-guiding, Tier 3 benchmark-required). Use this skill whenever someone asks how ready, mature, trustworthy, or deployable an AI-genomics tool, database, genomic-prediction pipeline, foundation model, pangenome method, or single-cell/regulatory model is for grass, cereal, forage, turf, bioenergy, or other Poaceae research or breeding — even if they don't name the framework — or asks whether a result supports breeding decisions versus hypothesis generation. Grounded in the manuscript-defined framework and its versioned supplementary data record on Zenodo (10.5281/zenodo.20825481).
---

# Grass AI-genomics readiness assessment

Judge how far an AI/bioinformatics result in grass genomics can responsibly be taken: to a decision, to a hypothesis, or back to the bench for benchmarking. The core idea the user relies on: **a tool is not ready because it scores well. It is ready only when the evidence holds for the exact use claimed.** The readiness tier is *derived from decision rules applied to four evidence gates* — never an average, a vibe, or a judgment of the paper's quality.

Assessments are bounded to a stated species, task, and user action, and reflect an evidence snapshot. The same model can be Tier 1 in one validated population and Tier 3 after transfer to another species.

## Reference files and scripts

Read the reference files rather than working from memory; run the scripts rather than deriving the tier by hand.

- **`references/rubric-definitions.md`** — the exact P/Pa/ND definitions for each gate, the leakage and action-type rules, and the ordered decision rules. **Read this every time before rating gates.**
- **`references/anchor-cases.md`** — the 18 expert-curated reference assessments (UC01–UC18) reported in the manuscript, with per-gate evidence and source locations. Use them as calibration.
- **`references/synthetic-boundary-tests.md`** — constructed rows (not literature cases) that exercise every decision rule, including the two that no real case reaches (Rule 3 and Rule 6/Tier 1).
- **`scripts/assign_tier.py`** — assigns the tier from the six inputs by fixed rules. **Always use this for final tier assignment once the gate ratings, leakage status, and action type are fixed.**
- **`scripts/validate_assessment.py`** — checks a completed assessment for internal consistency (every gate has evidence + a location; recorded tier matches the rules) and reproduces the reference sets.
- **`assets/assessment-template.json`** — the fillable structured-output template; complete it and validate it.

## Assessment mode — choose one before rating

The framework is a dated snapshot, but repositories and preprints move. Pick a mode explicitly and state it in the output:

1. **Snapshot reproduction.** Reproduce the manuscript assessment as of 2026-07-08. For any of UC01–UC18, use the anchor ratings unchanged. Do not alter them.
2. **Current-evidence reassessment.** Recheck the current paper, repository, licence, data, and model release, and re-rate all four gates on current evidence. Preserve the original anchor rating and report any change separately, with the recheck date. Use this when code has since opened, a preprint has become a version of record, or a licence has been added.

These are not in conflict: snapshot mode fixes the historical record; reassessment mode updates it without overwriting it.

## Workflow

### 1. Establish the bounded use case

A tier is meaningless without a bounded use case. Confirm all four before rating; ask for whatever is missing:

- **Tool / resource / study**, **species / evidence domain**, **stated task**, **intended user action**.

"Is this foundation model ready?" is not assessable. Narrow it with the user, or state the bounded case you are assuming and proceed on that basis.

### 2. Rate the four gates

Read `references/rubric-definitions.md`, then assign **P / Pa / ND** to each canonical gate from evidence you can point to — not the tool's reputation:

1. **Direct grass validation** (critical)
2. **Input transparency**
3. **Benchmark adequacy** (critical)
4. **Accessibility and reuse**

For each gate record three things separately: the **extracted evidence** (what the source actually reports), the **evidence location** (citation/DOI/page/table/figure/repository), and your **interpretation** (why that evidence maps to P/Pa/ND). Keeping evidence and location distinct from interpretation is what makes the assessment auditable rather than an opinion. If only an abstract is available, do not assign a final Pass to input transparency or benchmark adequacy — flag them for manual confirmation. Then record **leakage status** (No / Yes / Unclear / Not assessed) and the **action type** (`decision` or `explore`).

### 3. Assign the tier with the script

Do not derive the tier by hand. Run:

```
python scripts/assign_tier.py --dv <P|Pa|ND> --it <P|Pa|ND> --ba <P|Pa|ND> --ar <P|Pa|ND> --leakage <No|Yes|Unclear|Not assessed> --action <decision|explore>
```

It returns the tier and the single rule that fired. The rules that catch people: any leakage other than **No** forces Tier 3; a single critical-gate ND caps at Tier 2, both forces Tier 3; all four gates P with an exploratory action is still **Tier 2** (Rule 5); Tier 1 needs all-pass **and** a decision action, and is bounded.

### 4. Report and validate

Fill in `assets/assessment-template.json` and present this structure:

```
## Readiness: Tier N — label

### Bounded use case
- Tool/resource / Species or evidence domain / Stated task / Intended user action
- Assessment mode / Evidence snapshot (or recheck) date

### Gate assessment
| Gate | Rating | Extracted evidence | Evidence location | Interpretation |
| Direct grass validation | ... |
| Input transparency | ... |
| Benchmark adequacy | ... |
| Accessibility and reuse | ... |

### Decision
- Leakage status / Action type / Rule triggered / Assigned tier

### Boundary and uncertainty
- Supported use / Unsupported use / Missing or uncertain evidence / Minimum evidence to advance
```

Then run `python scripts/validate_assessment.py <your.json>` to confirm every gate has evidence and a location and that the recorded tier matches the rules. Keep the rationale tied to evidence and to the rule that fired; when the tier is 2 or 3, name the single thing most responsible (a missing critical gate, unresolved leakage, or an exploratory action) — that is what the user acts on.

## Guardrails

- **Bounded, not universal.** Never say a tool "is Tier N" without the use case. The tier travels with the stated species/task/action.
- **Derive, don't average.** Three passes and one ND is not "75% ready" — the ND may cap or sink the tier. Always run `assign_tier.py`.
- **Not a quality ranking.** Tier 3 is not a bad paper; it means the evidence for *this decision* is not yet there.
- **Snapshots move.** In current-evidence mode, recheck preprints and repositories and note the date; preserve the original anchor.
- **Stay in scope.** This rubric is calibrated for grass/Poaceae AI-genomics; for a use case far outside that domain, say the calibration may not transfer rather than forcing a tier.
- **Reproduce, then extend.** For any of the 18 reference cases, the anchor file is authoritative in snapshot mode. Assess beyond the anchors only for genuinely new use cases.

## Attribution

This skill operationalizes the readiness framework of Luo L, Sun Z, Lin Z, et al., "AI-driven grass genomics: an evidence-guided roadmap from bioinformatics resources to breeding decisions" (the accompanying manuscript; supplementary data record available from Zenodo, doi:10.5281/zenodo.20825481, CC-BY-4.0 data / MIT scripts). The 18 reference assessments are expert-curated, not independently re-validated. Assessments produced with this skill are interpretive aids, not authoritative endorsements, and should be checked against current evidence.
