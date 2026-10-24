# claim-evidence-kit

Plain templates for keeping public claims honest: write the test down before you run it, keep the failures, and only say what you can point to.

| File | What it is for |
|---|---|
| `templates/preregistration.md` | Write down the question, the measure, the pass bar and what would count as failure **before** looking at results |
| `templates/negative_results_ledger.md` | Keep every test that did not work, what was not tested, and how the idea could still work |
| `templates/claims_register.csv` | One row per public claim: its status and the evidence behind it |
| `check_claims.py` | Checks the register: every claim has a status, and anything marked `verified` points to its evidence |

## The four statuses

| Status | Meaning | May it be said publicly? |
|---|---|---|
| `verified` | Measured or documented; the evidence is linked | Yes, with the evidence |
| `assumed` | A planning figure or belief with nothing behind it yet | Only labelled as an assumption |
| `opinion` | A judgement or a choice | Only as an opinion |
| `retracted` | Was said, turned out wrong or unsupported | No; note what replaced it |

## Use

```bash
python check_claims.py templates/claims_register.csv
```

Exit code `0` when the register is clean, `1` with a list of problems otherwise. Python 3.9+, standard library only.

## Why

A result you cannot check is not a result yet. Writing the pass bar down first stops it moving after the numbers arrive, and keeping the failures stops the same dead end being explored twice.

Apache-2.0, see `LICENSE` and `NOTICE`.
