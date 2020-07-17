import unittest

from src.pow.solution import Solution


class TestPow(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_myPow_zero_raised_to_any_power_returns_zero(self):
        self._assert_myPow(0, 0, 12312)

    def test_myPow_one_raised_to_any_power_returns_one(self):
        self._assert_myPow(1, 1, 675)

    def test_myPow_negative_one_raised_to_an_even_power_returns_one(self):
        self._assert_myPow(1, -1, 16)

    def test_myPow_negative_one_raised_to_an_odd_power_returns_negative_one(self):
        self._assert_myPow(-1, -1, 17)

    def test_myPow_positive_number_raised_to_zero_returns_one(self):
        self._assert_myPow(1, 112, 0)

    def test_myPow_negative_number_raised_to_zero_returns_one(self):
        self._assert_myPow(1, -112, 0)
    
    def test_myPow_positive_number_raised_to_one_returns_itself(self):
        self._assert_myPow(324534, 324534, 1)

    def test_myPow_negative_number_raised_to_one_returns_itself(self):
        self._assert_myPow(-324534, -324534, 1)

    def test_myPow_whole_number_greater_than_one_raised_to_a_power_returns_a_greater_whole_number(self):
        self._assert_myPow(1024, 2, 10)

    def test_myPow_whole_number_raised_to_a_negative_power_returns_a_fraction(self):
        self._assert_myPow(0.25, 2, -2)

    def test_myPow_negative_whole_number_raised_to_a_even_negative_power_returns_a_positive_fraction(self):
        self._assert_myPow(0.25, -2, -2)

    def test_myPow_negative_whole_number_raised_to_an_odd_negative_power_returns_a_negative_fraction(self):
        self._assert_myPow(-0.125, -2, -3)

    def test_myPow_fractional_number_raised_to_a_positive_power_returns_a_greater_fractional_number(self):
        self._assert_myPow(9.261, 2.1, 3)

    def test_myPow_fractional_number_raised_to_a_negative_power_returns_a_fraction(self):
        self._assert_myPow(0.10798, 2.1, -3)

    def test_myPow_number_greater_than_one_raised_to_a_large_even_positive_power_returns_inf(self):
        self._assert_myPow(float('inf'), 2, 2147483647)

    def test_myPow_negative_number_greater_than_one_raised_to_a_large_even_positive_power_returns_inf(self):
        self._assert_myPow(float('inf'), -2, 2147483646)

    def test_myPow_negative_number_greater_than_one_raised_to_a_large_odd_positive_power_returns_negative_inf(self):
        self._assert_myPow(float('-inf'), -2, 2147483647)

    def test_myPow_number_greater_than_one_raised_to_a_large_negative_power_returns_zero(self):
        self._assert_myPow(0, 2, -2147483648)

    def test_myPow_small_fraction_large_positive_power_inf(self):
        self._assert_myPow(0, 0.00001, 2147483647)

    def test_myPow_small_positive_fraction_large_negative_power_return_inf(self):
        self._assert_myPow(float('inf'), 0.00001, -2147483648)

    def test_myPow_small_negative_fraction_large_even_negative_power_return_inf(self):
        self._assert_myPow(float('inf'), -0.00001, -2147483648)

    def test_myPow_small_negative_fraction_large_odd_negative_power_return_negative_inf(self):
        self._assert_myPow(float('-inf'), -0.00001, -2147483647)

    def _assert_myPow(self, expected: float, x: float, n: float) -> None:
        actual = self.solution.myPow(x, n)

        self.assertAlmostEqual(expected, actual, places=6)