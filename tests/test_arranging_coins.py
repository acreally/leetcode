import unittest

from src.arranging_coins.solution import Solution

class TestArrangingCoins(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_arrangeCoins_zero_coins_returns_zero_steps(self):
        self._assert_arrangeCoins(0, 0)

    def test_arrangeCoins_one_coin_returns_one_steps(self):
        self._assert_arrangeCoins(1, 1)

    def test_arrangeCoins_no_incomplete_steps_returns_number_of_steps(self):
        self._assert_arrangeCoins(3, 6)

    def test_arrangeCoins_incomplete_step_shorter_than_last_step_returns_number_of_complete_steps(self):
        self._assert_arrangeCoins(3, 8)

    def test_arrangeCoins_incomplete_step_same_length_as_last_step_returns_number_of_complete_steps(self):
        self._assert_arrangeCoins(3, 9)

    def test_arrangeCoins_max_value(self):
        self._assert_arrangeCoins(65535, 2147483647)

    def _assert_arrangeCoins(self, expected: int, n: int) -> None:
        actual = self.solution.arrangeCoins(n)

        self.assertEqual(expected, actual)