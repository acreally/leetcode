import unittest

from src.h_index_ii.solution import Solution
from typing import List


class TestHIndexII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_hIndex_citations_is_none_returns_none(self):
        self._assert_hIndex(None, None)

    def test_hIndex_citations_is_empty_returns_zero(self):
        self._assert_hIndex(0, [])

    def test_hIndex_only_publications_is_cited_zero_times_returns_zero(self):
        self._assert_hIndex(0, [0])

    def test_hIndex_only_publications_is_cited_more_than_one_time_returns_1(self):
        self._assert_hIndex(1, [1])

    def test_hIndex_only_publications_is_cited_more_than_one_times_returns_1(self):
        self._assert_hIndex(1, [4])

    def test_hIndex_number_of_publications_less_than_min_number_of_citations_returns_number_of_citations(self):
        self._assert_hIndex(3, [5, 6, 7])

    def test_hIndex_odd_number_of_publications_greater_than_max_number_of_citations_returns_ceiling_of_median_number_of_citations(self):
        self._assert_hIndex(3, [0, 1, 2, 3, 4, 5])

    def test_hIndex_even_number_of_publications_greater_than_max_number_of_citations_returns_median_number_of_citations(self):
        self._assert_hIndex(3, [0, 1, 2, 3, 4, 5, 6])

    def test_hIndex_number_of_citations_matches_exactly_returns_that_number_of_citations(self):
        self._assert_hIndex(3, [0, 1, 3, 5, 6])

    def test_hIndex_number_of_citations_does_not_match_exactly_returns_number_in_between(self):
        self._assert_hIndex(4, [0, 1, 3, 5, 6, 8, 9])

    def test_hIndex_more_publications_with_at_least_number_of_citations_but_no_publications_with_less(self):
        self._assert_hIndex(3, [3, 3, 5, 8, 25])

    def _assert_hIndex(self, expected: int, citations: List[int]) -> None:
        actual = self.solution.hIndex(citations)

        self.assertEqual(expected, actual)
