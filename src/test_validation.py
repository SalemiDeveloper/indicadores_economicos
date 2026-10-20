
import unittest
from datetime import date

from validation import validate_records


class TestValidation(unittest.TestCase):
    def test_valid_records(self):
        data = [
            {"data": "01/10/2026", "valor": "14.0"},
            {"data": "02/10/2026", "valor": "13.75"},
        ]

        result = validate_records(data, today=date(2026, 10, 20))

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["valor"], 14.0)
        self.assertEqual(result[0]["data"], "2026-10-01")

    def test_future_date(self):
        data = [
            {"data": "21/10/2026", "valor": "14.0"},
        ]

        with self.assertRaises(ValueError):
            validate_records(data, today=date(2026, 10, 20))

    def test_duplicate_dates(self):
        data = [
            {"data": "01/10/2026", "valor": "14.0"},
            {"data": "01/10/2026", "valor": "13.75"},
        ]

        with self.assertRaises(ValueError):
            validate_records(data, today=date(2026, 10, 20))

    
    def test_negative_value(self):
        data = [
            {"data": "01/10/2026", "valor": "-5"},
        ]

        with self.assertRaises(ValueError):
            validate_records(data, today=date(2026, 10, 20))

    def test_non_numeric_value(self):
        data = [
            {"data": "01/10/2026", "valor": "abc"},
        ]

        with self.assertRaises(ValueError):
            validate_records(data, today=date(2026, 10, 20))

    def test_invalid_date(self):
        data = [
            {"data": "32/10/2026", "valor": "14.0"},
        ]

        with self.assertRaises(ValueError):
            validate_records(data, today=date(2026, 10, 20))


if __name__ == "__main__":
    unittest.main()
