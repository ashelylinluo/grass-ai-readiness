# Synthetic boundary tests (NOT literature cases)

These rows are **constructed** rating combinations, not assessments of real studies. Their sole purpose is to demonstrate that every ordered decision rule is reachable and correctly implemented — including the two rules that no real use case in the current snapshot exercises:

- **Rule 3** (a single critical gate = ND) — not reached by any of UC01–UC18.
- **Rule 6** (all gates Pass + operational decision action = Tier 1) — not reached because the current assessment is 0 Tier 1 / 15 Tier 2 / 3 Tier 3.

Do **not** cite these as evidence about any tool, and do not mix them into the anchor set. They are executable checks on the rule engine.

The machine-checkable form is `synthetic-boundary-tests.tsv`; run `python scripts/assign_tier.py --selftest references/synthetic-boundary-tests.tsv` to confirm all rows reproduce.

| ID | DV | IT | BA | AR | Leakage | Action | Expected tier | Rule exercised |
|----|----|----|----|----|---------|--------|---------------|----------------|
| S01 | ND | P | P | P | No | decision | Tier 2 | Rule 3 — direct grass validation ND (single critical gate) caps at Tier 2 |
| S02 | P | P | ND | P | No | decision | Tier 2 | Rule 3 — benchmark adequacy ND (single critical gate) caps at Tier 2 |
| S03 | P | P | P | P | No | decision | Tier 1 | Rule 6 — all gates pass and action is operational decision support |
| S04 | P | P | P | P | No | explore | Tier 2 | Rule 5 — all gates pass but action is exploratory |
| S05 | P | P | P | P | Yes | decision | Tier 3 | Rule 1 — leakage present overrides an otherwise all-pass case |
| S06 | P | P | P | P | Not assessed | decision | Tier 3 | Rule 1 — leakage not assessed forces Tier 3 pending audit |
| S07 | ND | P | ND | P | No | explore | Tier 3 | Rule 2 — both critical gates ND |
| S08 | P | ND | P | P | No | decision | Tier 2 | Rule 4 — input transparency ND blocks Tier 1 but not Tier 3 |
| S09 | P | P | P | ND | No | decision | Tier 2 | Rule 4 — accessibility ND blocks Tier 1 but not Tier 3 |
| S10 | P | P | Pa | P | No | decision | Tier 2 | Rule 7 — a Partial with no ND and no leakage is hypothesis-guiding |
