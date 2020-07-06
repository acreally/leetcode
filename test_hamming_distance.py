import unittest

from src.hamming_distance.solution import Solution

class TestHammingDistance(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_same_number_returns_zero(self):
        self._assert_hammingDistance(0, 7, 7)

    def test_same_amount_of_bits_one_bit_off_returns_one(self):
        self._assert_hammingDistance(1, 7, 6)

    def test_same_amount_of_bits_two_bits_off_returns_two(self):
        self._assert_hammingDistance(2, 5, 6)

    def test_not_the_same_amount_of_bits_no_bits_match_returns_amount_of_bits_in_larger_number(self):
        self._assert_hammingDistance(5, 24, 7)

    def test_not_the_same_amount_of_bits_higher_order_bit_is_zero_returns_amount_of_bits_in_larger_number_less_one(self):
        self._assert_hammingDistance(4, 16, 7)

    def test_not_the_same_amount_of_bits_lower_order_bits_match_returns_one(self):
        self._assert_hammingDistance(1, 15, 7)

    def test_min_and_max_values(self):
        self._assert_hammingDistance(31, 0, 2147483647)

    def _assert_hammingDistance(self, expected: int, x: int, y: int) -> None:
        actual = self.solution.hammingDistance(x, y)

        self.assertEqual(expected, actual)
