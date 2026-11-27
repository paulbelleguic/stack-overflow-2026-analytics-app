"""Run with: uv run python -m unittest axes.axis_2.test_analysis."""
import unittest
import pandas as pd
from axes.axis_2.analysis import (
    USED, WANTED, VENDORS, choices, tool_ranking, paired_comparison,
    tool_count_distribution, selected_tool_details,
)

class ToolsAnalysisTest(unittest.TestCase):
    def setUp(self):
        self.frame = pd.DataFrame({
            'ResponseId': [1,2,3,4,5],
            USED: ['A; A ;B', 'B', None, 'A', '   '],
            WANTED: ['B;C','A', 'C', None, ''],
            VENDORS: ['Vendor',None,'Vendor',None,None],
        })

    def test_distinct_choices_and_question_denominators(self):
        table,n = tool_ranking(self.frame,USED)
        self.assertEqual(n,3)
        self.assertEqual(dict(zip(table.answer,table.respondents)), {'A':2,'B':2})
        self.assertAlmostEqual(table.share_pct.sum(),400/3)
        self.assertIsNone(choices(None))
        self.assertIsNone(choices(' '))

    def test_paired_base_excludes_one_sided_and_missing_lists(self):
        table,n = paired_comparison(self.frame)
        self.assertEqual(n,2)
        rows=table.set_index('answer')
        self.assertEqual(rows.loc['A','used_n'],1)
        self.assertEqual(rows.loc['B','used_n'],2)
        self.assertEqual(rows.loc['C','used_n'],0)
        self.assertEqual(rows.loc['C','wanted_pct'],50)
        self.assertEqual(rows.loc['B','difference_points'],-50)
        self.assertEqual(selected_tool_details(self.frame,'B'), {'paired_n':2,'used_n':2,'wanted_n':1,'both_n':1})

    def test_counts_exclude_unknowns_and_deduplicate(self):
        table,n=tool_count_distribution(self.frame)
        self.assertEqual(n,3)
        self.assertEqual(table.respondents.tolist(),[2,1,0,0])
        self.assertAlmostEqual(table.share_pct.sum(),100)

    def test_empty_and_unanswered_populations(self):
        for frame in [self.frame.iloc[:0], self.frame.iloc[[4]]]:
            for column in [USED,WANTED,VENDORS]:
                table,n=tool_ranking(frame,column)
                self.assertEqual(n,0)
                self.assertTrue(table.empty)
            comparison,n=paired_comparison(frame)
            self.assertEqual(n,0)
            self.assertTrue(comparison.empty)
            counts,n=tool_count_distribution(frame)
            self.assertEqual(n,0)
            self.assertEqual(counts.respondents.sum(),0)

if __name__ == '__main__':
    unittest.main()
