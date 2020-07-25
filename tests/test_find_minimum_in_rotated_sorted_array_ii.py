import unittest

from typing import List

from src.find_minimum_in_rotated_sorted_array_ii.solution import Solution


class TestFindMinimumInRotatedSortedArrayII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_findMin_one_element_returns_that_element(self):
        self._assert_findMin(123, [123])

    def test_findMin_in_order_list_no_dupes_returns_first_item(self):
        self._assert_findMin(1, [1, 2, 3, 4])

    def test_findMin_rotated_list_min_item_in_middle_no_dupes_returns_min_item(self):
        self._assert_findMin(1, [4, 5, 1, 2, 3])

    def test_findMin_rotated_list_min_item_at_end_no_dupes_returns_min_item(self):
        self._assert_findMin(1, [2, 3, 4, 5, 1])

    def test_findMin_in_order_list_dupes_min_item_not_duped_returns_first_item(self):
        self._assert_findMin(1, [1, 2, 3, 3, 4, 4, 4, 4])

    def test_findMin_in_order_list_dupes_min_item_duped_returns_first_item(self):
        self._assert_findMin(1, [1, 1, 2, 3, 3, 4, 4, 4, 4])

    def test_findMin_in_order_list_dupes_min_item_duped_only_item_returns_min_item(self):
        self._assert_findMin(1, [1, 1, 1, 1, 1, 1])

    def test_findMin_rotated_list_dupes_min_item_not_duped_min_item_in_middle_returns_min_item(self):
        self._assert_findMin(0, [2, 2, 2, 0, 1])

    def test_findMin_rotated_list_dupes_min_item_duped_min_item_in_middle_returns_first_item(self):
        self._assert_findMin(1, [4, 4, 4, 4, 1, 1, 1, 2, 3, 3])

    def test_findMin_rotated_list_dupes_min_item_not_duped_min_item_at_end_returns_min_item(self):
        self._assert_findMin(1, [2, 2, 3, 3, 4, 4, 4, 4, 1])

    def test_findMin_rotated_list_dupes_min_item_not_duped_all_other_items_the_same_returns_min_item(self):
        self._assert_findMin(1, [10, 1, 10, 10, 10])

    def test_findMin_rotated_list_dupes_min_item_duped_min_item_at_end_returns_first_item(self):
        self._assert_findMin(1, [2, 3, 3, 4, 4, 4, 4, 1, 1, 1])

    def test_findMin_in_order_list_no_dupes_long_list_returns_first_item(self):
        self._assert_findMin(1, [i for i in range(1, 1000)])

    def test_findMin_in_order_list_dupes_min_item_duped_only_item_long_list_returns_min_item(self):
        self._assert_findMin(1, [1] * 100000000)

    def _assert_findMin(self, expected: int, nums: List[int]) -> None:
        actual = self.solution.findMin(nums)

        self.assertEqual(expected, actual)
