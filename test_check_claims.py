import csv
import pathlib
import unittest

import check_claims

HERE = pathlib.Path(__file__).parent


class ClaimTests(unittest.TestCase):
    def test_example_register_is_clean(self):
        with open(HERE / "templates" / "claims_register.csv", newline="", encoding="utf-8") as fh:
            self.assertEqual(check_claims.check(list(csv.DictReader(fh))), [])

    def test_verified_needs_evidence(self):
        rows = [{"id": "C-1", "claim": "x", "status": "verified", "evidence": "", "notes": ""}]
        self.assertTrue(any("no evidence" in p for p in check_claims.check(rows)))

    def test_bad_status_and_duplicate(self):
        rows = [{"id": "C-1", "claim": "x", "status": "proven", "evidence": "", "notes": ""},
                {"id": "C-1", "claim": "y", "status": "opinion", "evidence": "", "notes": ""}]
        problems = check_claims.check(rows)
        self.assertTrue(any("not one of" in p for p in problems))
        self.assertTrue(any("duplicate" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
