import unittest

from src.add_digits.solution import Solution


class TestAddDigits(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_addDigits_zero_returns_zero(self):
        self._assert_addDigits(0, 0)

    def test_addDigits_number_less_than_base_returns_number(self):
        self._assert_addDigits(9, 9)

    def test_addDigits_digits_add_to_number_less_than_base(self):
        self._assert_addDigits(6, 15)

    def test_addDigits_digits_add_to_number_more_than_base(self):
        self._assert_addDigits(2, 38)

    def test_addDigits_large_number(self):
        self._assert_addDigits(9, 123456789)

    def _assert_addDigits(self, expected: int, num: int) -> None:
        actual = self.solution.addDigits(num)

        self.assertEqual(expected, actual)
