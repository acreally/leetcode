import unittest

from typing  import List

from src.top_k_frequent_elements.solution import Solution


class TestTopKFrequentElements(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_topKFrequent_empty_list_returns_empty_list(self):
        self._assert_topKFrequent([], [], 0)

    def test_topKFrequent_one_element_returns_that_element(self):
        self._assert_topKFrequent([1], [1], 1)

    def test_topKFrequent_all_unique_elements_returns_all_elements(self):
        self._assert_topKFrequent([1, 2, 3, 4], [1, 2, 3, 4], 4)

    def test_topKFrequent_most_frequent_elements_at_end_of_list(self):
        self._assert_topKFrequent([4, 5, 6], [1, 2, 3, 4, 4, 5, 5, 5, 6, 6], 3)

    def test_topKFrequent_most_frequent_elements_in_middle_of_list(self):
        self._assert_topKFrequent([3, 5], [1, 2, 3, 3, 3, 4, 5, 5, 5, 6], 2)

    def test_topKFrequent_most_frequent_elements_with_same_frequency_returns_all_of_must_frequent_elements(self):
        self._assert_topKFrequent([1, 2], [1, 1, 2, 2, 3, 4], 2)

    def test_topKFrequent_most_frequent_elements_with_different_frequency_returns_all_of_must_frequent_elements(self):
        self._assert_topKFrequent([1, 2, 3], [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7], 3)

    def test_topKFrequent_long_list(self):
        self._assert_topKFrequent([1], [i for i in range(10000000)] + [1], 1)

    def _assert_topKFrequent(self, expected: List[int], nums: List[int], k: int) -> None:
        actual = self.solution.topKFrequent(nums, k)

        self.assertEqual(len(expected), len(actual))
        for i in expected:
            self.assertTrue(i in actual)
