#!/usr/bin/env python3
"""assign_tier.py — deterministic readiness-tier assignment.

The language model reads the evidence and assigns each gate a rating
(P / Pa / ND), a leakage status, and an action type. THIS script then
assigns the tier by fixed rules only. The tier is never a model judgment
or an average — it is a pure function of the six inputs below.

Inputs
------
  dv, it, ba, ar : one of "P", "Pa", "ND"
      Gate 1 Direct grass validation, Gate 2 Input transparency,
      Gate 3 Benchmark adequacy, Gate 4 Accessibility and reuse.
  leakage        : one of "No", "Yes", "Unclear", "Not assessed"
  action         : one of "decision", "explore"
      "decision" = operational decision support (ranking, selection,
      calibrated trait extraction). "explore" = hypothesis, mechanism,
      or benchmark work.

Output
------
  A dict with the assigned tier and the single rule that determined it.

Usage
-----
  # as a module
  from assign_tier import assign_tier
  assign_tier("P","P","P","P","No","decision")

  # from the command line
  python assign_tier.py --dv P --it P --ba P --ar P --leakage No --action decision

  # self-test against the anchor and synthetic reference sets
  python assign_tier.py --selftest anchor-cases.tsv synthetic-boundary-tests.tsv
"""
from __future__ import annotations
import argparse, csv, sys

GATE_VALUES = {"P", "Pa", "ND"}
LEAK_VALUES = {"No", "Yes", "Unclear", "Not assessed"}
ACTION_VALUES = {"decision", "explore"}

TIER_LABEL = {
    "Tier 1": "decision-support ready",
    "Tier 2": "hypothesis-guiding",
    "Tier 3": "benchmark-required",
}


def _validate(dv, it, ba, ar, leakage, action):
    for name, val, allowed in (
        ("dv", dv, GATE_VALUES), ("it", it, GATE_VALUES),
        ("ba", ba, GATE_VALUES), ("ar", ar, GATE_VALUES),
        ("leakage", leakage, LEAK_VALUES), ("action", action, ACTION_VALUES),
    ):
        if val not in allowed:
            raise ValueError(f"{name}={val!r} is not one of {sorted(allowed)}")


def assign_tier(dv, it, ba, ar, leakage, action):
    """Return {'tier', 'label', 'rule', 'explanation'} by fixed rules.

    Rules are applied top to bottom; the first that applies decides.
    """
    _validate(dv, it, ba, ar, leakage, action)
    ND = "ND"

    # Rule 1 — leakage
    if leakage in ("Yes", "Unclear", "Not assessed"):
        return _out("Tier 3", "Rule 1 (leakage)",
                    f"Leakage status is '{leakage}'; any value other than 'No' "
                    "forces Tier 3 until a leakage audit resolves it.")

    # Rule 2 — both critical gates fail
    if dv == ND and ba == ND:
        return _out("Tier 3", "Rule 2 (both critical gates ND)",
                    "Direct grass validation and benchmark adequacy are both "
                    "Not demonstrated.")

    # Rule 3 — one critical gate fails
    if dv == ND or ba == ND:
        which = "Direct grass validation" if dv == ND else "Benchmark adequacy"
        return _out("Tier 2", "Rule 3 (one critical gate ND)",
                    f"{which} is Not demonstrated, which caps the case at Tier 2; "
                    "strength in other gates cannot compensate for a missing "
                    "critical gate.")

    all_pass = dv == "P" and it == "P" and ba == "P" and ar == "P"
    if all_pass:
        # Rule 6 — Tier 1
        if action == "decision":
            return _out("Tier 1", "Rule 6 (all pass + decision action)",
                        "All four gates pass and the stated action is operational "
                        "decision support; Tier 1 is bounded to the stated species, "
                        "population, environment, task and action.")
        # Rule 5 — all pass but exploratory
        return _out("Tier 2", "Rule 5 (all pass + exploratory action)",
                    "All four gates pass, but the stated action is hypothesis, "
                    "mechanism or benchmark work rather than operational decision "
                    "support, so the case is capped at Tier 2.")

    # Rule 4 / Rule 7 — non-critical ND blocks Tier 1 but not Tier 3; or Partials only
    if it == ND or ar == ND:
        return _out("Tier 2", "Rule 4 (non-critical ND)",
                    "A non-critical gate (input transparency or accessibility and "
                    "reuse) is Not demonstrated; this blocks Tier 1 but does not by "
                    "itself trigger Tier 3.")
    return _out("Tier 2", "Rule 7 (default)",
                "One or more gates are Partial with no ND and no leakage, so the "
                "case is hypothesis-guiding.")


def _out(tier, rule, explanation):
    return {"tier": tier, "label": TIER_LABEL[tier], "rule": rule,
            "explanation": explanation}


def _selftest(paths):
    """Check every row of the given TSV reference sets reproduces.

    Each TSV must have a header with columns:
      id, dv, it, ba, ar, leakage, action, expected_tier
    """
    total = fails = 0
    for path in paths:
        with open(path, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                total += 1
                got = assign_tier(row["dv"], row["it"], row["ba"], row["ar"],
                                  row["leakage"], row["action"])["tier"]
                exp = row["expected_tier"].strip()
                if got != exp:
                    fails += 1
                    print(f"MISMATCH {row['id']}: got {got}, expected {exp}")
    print(f"\n{total - fails}/{total} rows reproduce"
          + ("" if fails else "  — all consistent."))
    return fails == 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dv"); p.add_argument("--it")
    p.add_argument("--ba"); p.add_argument("--ar")
    p.add_argument("--leakage"); p.add_argument("--action")
    p.add_argument("--selftest", nargs="+", metavar="TSV",
                   help="reproduce tiers for the given reference TSV sets")
    a = p.parse_args(argv)

    if a.selftest:
        return 0 if _selftest(a.selftest) else 1

    if not all([a.dv, a.it, a.ba, a.ar, a.leakage, a.action]):
        p.error("provide all of --dv --it --ba --ar --leakage --action, "
                "or use --selftest")
    r = assign_tier(a.dv, a.it, a.ba, a.ar, a.leakage, a.action)
    print(f"{r['tier']} — {r['label']}")
    print(f"Rule: {r['rule']}")
    print(f"Why:  {r['explanation']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # output was piped into a command that closed early (e.g. `head`)
        sys.exit(0)
