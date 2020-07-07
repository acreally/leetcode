import unittest

from typing import List

from src.plus_one.solution import Solution

class TestPlusOne(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_plusOne_zero_returns_one(self):
        self._assert_plusOne([1], [0])

    def test_plusOne_no_carry_over(self):
        self._assert_plusOne([1, 2, 4], [1, 2, 3])

    def test_plusOne_carry_over_from_least_significant_digit_only(self):
        self._assert_plusOne([1, 3, 0], [1, 2, 9])

    def test_plusOne_carry_over_from_all_but_most_significant_digit(self):
        self._assert_plusOne([2, 0, 0], [1, 9, 9])

    def test_plusOne_carry_over_from_all_digits(self):
        self._assert_plusOne([1, 0, 0, 0], [9, 9, 9])

    def test_plusOne_carry_over_from_all_digits_big_number(self):
        self._assert_plusOne([1] + [0] * 100000000, [9] * 100000000)

    def _assert_plusOne(self, expected: List[int], digits: List[int]) -> None:
        actual = self.solution.plusOne(digits)

        self.assertEqual(expected, actual)