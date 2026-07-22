#!/usr/bin/env python3
"""validate_assessment.py — check a completed assessment for internal consistency.

Two jobs:

1. Structural + rule check on a single assessment JSON (the shape in
   assets/assessment-template.json). Confirms every gate has a rating,
   evidence, and a location; that leakage/action are valid; and that the
   recorded tier equals what assign_tier.py derives from the ratings —
   so a human-written tier can never silently disagree with the rules.

2. Reference-set check: reproduce every row of the anchor and synthetic
   reference TSVs. This is the "does the engine still hold" regression.

Usage
-----
  python validate_assessment.py my_assessment.json
  python validate_assessment.py --references references/
"""
from __future__ import annotations
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assign_tier import assign_tier, GATE_VALUES, LEAK_VALUES, ACTION_VALUES  # noqa: E402

CANONICAL_GATES = [
    "Direct grass validation", "Input transparency",
    "Benchmark adequacy", "Accessibility and reuse",
]
GATE_KEY = {"Direct grass validation": "dv", "Input transparency": "it",
            "Benchmark adequacy": "ba", "Accessibility and reuse": "ar"}
VALID_MODES = {"snapshot_reproduction", "current_evidence_reassessment"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLACEHOLDER = "filled by scripts/assign_tier.py"


def check_assessment(path):
    with open(path, encoding="utf-8") as fh:
        a = json.load(fh)
    errs, warns = [], []

    uc = a.get("bounded_use_case", {})
    for f in ("tool_or_resource", "species_or_evidence_domain",
              "stated_task", "intended_user_action"):
        if not uc.get(f):
            errs.append(f"bounded_use_case.{f} is empty — the tier would be unbounded")
    mode = uc.get("assessment_mode", "")
    if mode not in VALID_MODES:
        errs.append(f"assessment_mode {mode!r} is not one of {sorted(VALID_MODES)}")
    snap = uc.get("evidence_snapshot_date", "")
    if not DATE_RE.match(snap or ""):
        errs.append(f"evidence_snapshot_date {snap!r} is not YYYY-MM-DD")

    gates = a.get("gate_assessment", [])
    names = [g.get("gate") for g in gates]
    if names != CANONICAL_GATES:
        errs.append(f"gates must be exactly {CANONICAL_GATES} in order; got {names}")

    ratings = {}
    for g in gates:
        gn = g.get("gate"); r = g.get("rating")
        if r not in GATE_VALUES:
            errs.append(f"{gn}: rating {r!r} not in {sorted(GATE_VALUES)}")
        else:
            ratings[GATE_KEY.get(gn, gn)] = r
        if not g.get("extracted_evidence"):
            errs.append(f"{gn}: extracted_evidence is empty")
        if not g.get("evidence_location"):
            errs.append(f"{gn}: evidence_location is empty — assessment is not auditable")
        if not g.get("interpretation"):
            errs.append(f"{gn}: interpretation is empty — evidence is not tied to the rating")

    dec = a.get("decision", {})
    leak = dec.get("leakage_status"); act = dec.get("action_type")
    if leak not in LEAK_VALUES:
        errs.append(f"leakage_status {leak!r} not in {sorted(LEAK_VALUES)}")
    if act not in ACTION_VALUES:
        errs.append(f"action_type {act!r} not in {sorted(ACTION_VALUES)}")

    # the core auditability check: recorded tier AND rule must match the engine
    if not errs and all(k in ratings for k in ("dv", "it", "ba", "ar")):
        derived = assign_tier(ratings["dv"], ratings["it"], ratings["ba"],
                              ratings["ar"], leak, act)
        recorded = (dec.get("assigned_tier") or "").strip()
        if not recorded or recorded == PLACEHOLDER:
            errs.append(f"assigned_tier is empty — run assign_tier.py and record its "
                        f"output (rules give {derived['tier']}, {derived['rule']})")
        elif recorded != derived["tier"]:
            errs.append(f"assigned_tier {recorded!r} disagrees with the rules "
                        f"({derived['tier']}, {derived['rule']}) — the tier must "
                        "be the rule output, not a separate judgment")
        rule_rec = (dec.get("rule_triggered") or "").strip()
        if rule_rec and rule_rec != PLACEHOLDER:
            # accept if the recorded rule names the same rule the engine fired
            engine_rule = derived["rule"].split(" ")[0] + " " + derived["rule"].split(" ")[1]
            if not rule_rec.startswith(engine_rule.rstrip("(")):
                warns.append(f"rule_triggered {rule_rec!r} does not match the engine "
                             f"rule ({derived['rule']})")

    bu = a.get("boundary_and_uncertainty", {})
    for f in ("supported_use", "unsupported_use", "minimum_evidence_to_advance"):
        if not bu.get(f):
            warns.append(f"boundary_and_uncertainty.{f} is empty")

    return errs, warns


def check_references(ref_dir):
    import csv
    total = fails = 0
    for name in ("anchor-cases.tsv", "synthetic-boundary-tests.tsv"):
        path = os.path.join(ref_dir, name)
        if not os.path.exists(path):
            print(f"(skip: {name} not found in {ref_dir})")
            continue
        with open(path, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                total += 1
                got = assign_tier(row["dv"], row["it"], row["ba"], row["ar"],
                                  row["leakage"], row["action"])["tier"]
                if got != row["expected_tier"].strip():
                    fails += 1
                    print(f"MISMATCH {row['id']}: got {got}, "
                          f"expected {row['expected_tier']}")
    print(f"{total - fails}/{total} reference rows reproduce"
          + ("" if fails else "  — engine consistent."))
    return fails == 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("assessment", nargs="?", help="assessment JSON to check")
    p.add_argument("--references", metavar="DIR",
                   help="reproduce anchor + synthetic reference sets in DIR")
    a = p.parse_args(argv)

    ok = True
    if a.references:
        ok = check_references(a.references) and ok
    if a.assessment:
        errs, warns = check_assessment(a.assessment)
        for w in warns:
            print(f"WARN  {w}")
        for e in errs:
            print(f"ERROR {e}")
        if not errs:
            print(f"OK    {a.assessment} is internally consistent"
                  + (f" ({len(warns)} warnings)" if warns else ""))
        ok = ok and not errs
    if not a.references and not a.assessment:
        p.error("provide an assessment JSON, --references DIR, or both")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
