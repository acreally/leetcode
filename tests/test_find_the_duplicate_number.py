import unittest

from src.find_the_duplicate_number.solution import Solution
from typing import List


class TestFindTheDuplicateNumber(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_findDuplicate_duplicates_are_at_the_end(self):
        self._assert_findDuplicate(2, [1,3,4,2,2])

    def test_findDuplicate_duplicates_are_at_the_start(self):
        self._assert_findDuplicate(1, [1,1,3,4,2])

    def test_findDuplicate_duplicates_are_at_the_start_and_end(self):
        self._assert_findDuplicate(1, [1,3,4,2,1])

    def test_findDuplicate_duplicates_are_in_the_middle_adjacent(self):
        self._assert_findDuplicate(4, [1,3,4,4,2,5])

    def test_findDuplicate_duplicates_are_in_the_middle_not_adjacent(self):
        self._assert_findDuplicate(4, [1,3,4,5,2,4,6,7])

    def test_findDuplicate_duplicate_repeated_more_than_once(self):
        self._assert_findDuplicate(4, [1,3,4,4,2,4,6,4])

    def test_findDuplicate_not_that_long_of_a_list(self):
        self._assert_findDuplicate(1, [i for i in range(1, 1000000 // 2)] + [1])

    def test_findDuplicate_long_list(self):
        self._assert_findDuplicate(1, [i for i in range(1, 1000000)] + [1])

    # def test_findDuplicate_really_long_list(self):
    #     self._assert_findDuplicate(1, [i for i in range(1, 10000000)] + [1])

    def _assert_findDuplicate(self, expected: int, nums: List[int]) -> None:
        actual = self.solution.findDuplicate(nums)

        self.assertEqual(expected, actual)