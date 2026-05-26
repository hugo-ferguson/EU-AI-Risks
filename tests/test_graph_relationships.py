import unittest

from eu_ai_risks.db.graph import sanitize_affected_by_rows


class SanitizeAffectedByRowsTests(unittest.TestCase):
	def test_filters_blank_values_and_deduplicates(self):
		records = [
			{"title": "Requirement 1", "paragraph_id": "par:1"},
			{"title": "Requirement 1", "paragraph_id": "par:1"},
			{"title": "  Requirement 2  ", "paragraph_id": " par:2 "},
			{"title": "", "paragraph_id": "par:3"},
			{"title": "Requirement 3", "paragraph_id": ""},
		]

		result = sanitize_affected_by_rows(records)

		self.assertEqual(
			result,
			[
				{"title": "Requirement 1", "paragraph_id": "par:1"},
				{"title": "Requirement 2", "paragraph_id": "par:2"},
			],
		)


if __name__ == "__main__":
	unittest.main()
