# Readiness rubric: gate definitions and decision rules

Authoritative rubric from the manuscript's supplementary materials (Supplementary Table S5, Rubric worksheet). Rate every gate against these definitions, then let the decision rules assign the tier. The tier is *derived from the rules*, never averaged or eyeballed. For the tier assignment itself, use `scripts/assign_tier.py`, which implements these rules exactly.

## The four gates (canonical names)

Always use these four names, in this order and wording:

1. **Direct grass validation** (critical)
2. **Input transparency**
3. **Benchmark adequacy** (critical)
4. **Accessibility and reuse**

## Unit of assessment

Score a **bounded use case**, never a broad method family in isolation. A bounded use case is:

> tool / resource + species or evidence domain + stated task + intended user action

If any of these four is missing, ask for it before rating. "Is a genome foundation model ready?" is not assessable; "Are AgroNT embeddings ready for ranking candidate promoters in switchgrass, to prioritize follow-up experiments?" is. The use case may be narrowly scoped (a specific tool, dataset, and endpoint); the rubric assesses that scoped use, not the method family it belongs to.

## Gate definitions

### Gate 1 — Direct grass validation (CRITICAL)
- **P (Pass):** Direct validation in the target grass/context, and the tested endpoint matches the claimed action.
- **Pa (Partial):** Grass/Poaceae evidence exists, but species, population, environment, or endpoint is only partly matched.
- **ND (Not demonstrated):** No direct grass/context evidence, or only general plant / human / generic-benchmark evidence.

### Gate 2 — Input transparency
- **P:** Genome/pangenome version, samples, markers/sequence, phenotype/environment, preprocessing, and data splits are traceable.
- **Pa:** Most inputs are described, but one or more key elements are incomplete.
- **ND:** Critical inputs, preprocessing, or splits cannot be reconstructed.
- **Manual-check rule:** If only an abstract is available, or the full text has not been read, treat input transparency as requiring manual confirmation rather than assigning a final Pass.

### Gate 3 — Benchmark adequacy (CRITICAL)
- **P:** Claim-matched split, an appropriate simple/standard baseline, leakage control, task-appropriate metrics, and a relevant held-out test.
- **Pa:** A benchmark exists, but external validation, calibration, failure analysis, or claim-matched splitting is incomplete.
- **ND:** No task-matched benchmark/baseline, unresolved leakage, or a random/internal split is used to support a broad transfer/deployment claim.
- **Manual-check rule:** Same abstract-only caveat as Gate 2.

### Gate 4 — Accessibility and reuse
- **P:** Data/code/weights/tool, versioning, documentation, and licence are sufficient for reasonable reuse.
- **Pa:** Some components are available, but weights, data, code, version, licence, or documentation are incomplete.
- **ND:** Workflow/tool/data are unavailable or non-reconstructable.
- **Non-compensation:** Accessibility cannot compensate for weak validation. Open code does not raise a case whose biological evidence is weak.

## Leakage status

Record leakage independently: **No / Yes / Unclear / Not assessed**. Values of **Yes, Unclear, or Not assessed** are treated conservatively as Tier-3 triggers pending an audit. Only **No** (controlled, or not a concern) keeps a case out of the leakage-triggered Tier 3.

## Action type

Classify the stated user action as one of:
- **decision** — operational decision support, e.g. parent/line/environment ranking, genomic selection within the evaluated population, or calibrated trait extraction feeding a decision.
- **explore** — hypothesis, mechanism, or benchmark work: prioritizing candidate genes or sequences, interpreting a mechanism, or building/evaluating a benchmark.

This classification matters only when all four gates pass (see Rule 5 vs Rule 6). It is the rule that keeps a well-documented *exploratory* study from being relabelled a breeding-decision tool.

## Decision rules (apply in order; first match wins)

1. **Leakage → Tier 3.** If leakage status is Yes, Unclear, or Not assessed, the case is **Tier 3** until a leakage audit resolves it. No combination of gate passes overrides this.
2. **Both critical gates fail → Tier 3.** If Direct grass validation = ND **and** Benchmark adequacy = ND, the case is **Tier 3**.
3. **One critical gate fails → cap at Tier 2.** If Direct grass validation = ND **or** Benchmark adequacy = ND (but not both), the case is capped at **Tier 2**. Strength elsewhere cannot compensate for a missing critical gate.
4. **Non-critical ND blocks Tier 1 only.** An ND on Input transparency or Accessibility and reuse blocks Tier 1 but does **not** by itself trigger Tier 3. Such a case lands at **Tier 2**.
5. **All gates pass, but exploratory action → cap at Tier 2.** If all four gates are P but the stated action is hypothesis, mechanism, or benchmark work, the case is **Tier 2**.
6. **Tier 1.** Only if all four gates are P **and** the stated action is operational decision support. Tier 1 is **bounded** to the stated species, population, environment, task, and action — it is not a general endorsement, autonomous deployment, or licence to transfer.
7. **Otherwise → Tier 2.** Any remaining case (e.g. one or more Partial ratings, no ND, leakage No) is **Tier 2**, hypothesis-guiding.

Rules 3 and 6 are not exercised by any of the 18 reference cases (the snapshot is 0 Tier 1 / 15 Tier 2 / 3 Tier 3). `references/synthetic-boundary-tests.md` supplies constructed rows that exercise every rule, so the engine can be verified end to end.

## Tier meanings

- **Tier 1 — decision-support ready:** Supports the specified user action under the validated conditions, bounded to those conditions.
- **Tier 2 — hypothesis-guiding:** Supports prioritization, interpretation, or experimental design within the stated boundary. Tier 2 is *not* a general quality judgment.
- **Tier 3 — benchmark-required:** Technically promising, but stronger task-specific validation is required before it can guide biological or breeding choices.

## Versioning caveat

Assessments are snapshots. Preprints and repositories must be rechecked immediately before any reuse; a tier can move as evidence, code, or benchmarks change. When re-rating against newer evidence, work in current-evidence reassessment mode (see SKILL.md) and keep the original snapshot rating alongside the update.

## What this rubric is not

Ratings are use-case-specific and are **not** rankings of papers, tools, developers, or overall scientific quality. A cereal workflow can sit at Tier 3 if its trait/stress/tissue/decision lacks validation, while a narrow, well-curated within-population task in a non-model grass may approach Tier 1. The tier travels with the stated use case, not with the method.
