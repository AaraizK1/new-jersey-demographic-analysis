import csv
import tempfile
import unittest
from pathlib import Path

from main import load_data, estimated_count, validate_totals, DEFAULT_DATA


class DemographicsTests(unittest.TestCase):
    def test_original_2024_population_estimate(self):
        self.assertEqual(estimated_count(17.91, 9_320_860), 1_669_366)

    def test_load_categories(self):
        data = load_data(DEFAULT_DATA)
        self.assertEqual(len(data["Age"]), 5)
        self.assertEqual(len(data["Gender"]), 2)

    def test_valid_totals(self):
        data = load_data(DEFAULT_DATA)
        warnings = validate_totals(data)
        self.assertTrue(any("Education" in w for w in warnings))
        self.assertTrue(any("Career" in w for w in warnings))

    def test_reject_invalid_percentage(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.csv"
            path.write_text("category,group,percentage\\nAge,Adults,110\\n")
            with self.assertRaises(ValueError):
                load_data(path)


if __name__ == "__main__":
    unittest.main()
