import unittest

from typing import List

from src.three_sum.solution import Solution


class TestThreeSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_threeSum_empty_list_returns_empty_list(self):
        self._assert_threeSum([], [])

    def test_threeSum_no_answer_returns_empty_list(self):
        self._assert_threeSum([], [1, 2, 3])

    def test_threeSum_single_answer_returns_one_answer(self):
        self._assert_threeSum([[-1, 0, 1]], [-1, 0, 1])

    def test_threeSum_multiple_answers_only_with_overlap_returns_one_answer(self):
        self._assert_threeSum([[-1, 0, 1]], [-1, 0, 1, 0, 1])

    def test_threeSum_multiple_answers_with_no_overlap_returns_multiple_answers(self):
        self._assert_threeSum([[-1, 0, 1], [2, 4, -6]], [-1, 0, 1, 2, 4, -6])

    def test_threeSum_large_list_single_answer_at_then_end_returns_single_answer(self):
        self._assert_threeSum([[-1, 0, 1]], [2, 3, 4] * 1000 + [-1, 0, 1])

    def _assert_threeSum(self, expected: List[List[int]], nums: List[int]) -> None:
        actual = self.solution.threeSum(nums)

        self.assertEqual(expected, actual)
