"""check_claims: check a claims register CSV.

Rules: every row has an id, a claim and a status from {verified, assumed, opinion, retracted};
ids are unique; a verified claim names its evidence; a retracted claim says what replaced it or why.

Usage:
    python check_claims.py claims_register.csv
"""
import csv
import sys

STATUSES = {"verified", "assumed", "opinion", "retracted"}


def check(rows):
    problems, seen = [], set()
    for n, row in enumerate(rows, start=2):
        cid = (row.get("id") or "").strip()
        status = (row.get("status") or "").strip().lower()
        if not cid:
            problems.append(f"line {n}: no id")
        elif cid in seen:
            problems.append(f"line {n}: duplicate id {cid}")
        seen.add(cid)
        if not (row.get("claim") or "").strip():
            problems.append(f"line {n} ({cid}): no claim text")
        if status not in STATUSES:
            problems.append(f"line {n} ({cid}): status '{status}' is not one of {sorted(STATUSES)}")
        if status == "verified" and not (row.get("evidence") or "").strip():
            problems.append(f"line {n} ({cid}): verified but no evidence")
        if status == "retracted" and not (row.get("notes") or "").strip():
            problems.append(f"line {n} ({cid}): retracted but no note on why or what replaced it")
    return problems


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    if len(argv) != 1:
        print(__doc__)
        return 2
    with open(argv[0], newline="", encoding="utf-8-sig") as fh:
        problems = check(list(csv.DictReader(fh)))
    if problems:
        print("Problems:\n- " + "\n- ".join(problems))
        return 1
    print("Register is clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
