import unittest

from src.add_binary.solution import Solution


class TestAddBinary(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_addBinary_both_numbers_are_zero_returns_zero(self):
        self._assert_addBinary('0', '0', '0')

    def test_addBinary_first_number_is_zero_returns_second_number(self):
        self._assert_addBinary('101', '0', '101')

    def test_addBinary_second_number_is_zero_returns_first_number(self):
        self._assert_addBinary('11101', '11101', '0')

    def test_addBinary_both_numbers_have_same_number_of_digits(self):
        self._assert_addBinary('101111', '11101', '10010')

    def test_addBinary_first_number_has_more_digits_no_carry_over(self):
        self._assert_addBinary('11111', '10101', '1010')

    def test_addBinary_first_number_has_more_digits_with_carry_over(self):
        self._assert_addBinary('100111', '11101', '1010')

    def test_addBinary_second_number_has_more_digits_no_carry_over(self):
        self._assert_addBinary('111101', '10101', '101000')

    def test_addBinary_second_number_has_more_digits_with_carry_over(self):
        self._assert_addBinary('1010101', '11101', '111000')

    def test_addBinary_first_number_is_max_value_second_number_is_one(self):
        self._assert_addBinary('1' + '0' * 10**4, '1' * 10**4, '1')

    def test_addBinary_second_number_is_max_value_first_number_is_one(self):
        self._assert_addBinary('1' + '0' * 10**4, '1', '1' * 10**4)

    def test_addBinary_both_numbers_are_max_value(self):
        self._assert_addBinary('1' * 10**4  + '0', '1' * 10**4, '1' * 10**4)

    def _assert_addBinary(self, expected: str, a: str, b: str) -> None:
        actual = self.solution.addBinary(a, b)

        self.assertEqual(expected, actual)
