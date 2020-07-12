import unittest

from src.reverse_bits.solution import Solution


class TestReverseBits(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverseBits_zero(self):
        self._assert_reverseBits(0, 0)

    def test_reverseBits_example_one(self):
        self._assert_reverseBits(964176192, 10100101000001111010011100)

    def test_reverseBits_example_two(self):
        self._assert_reverseBits(3221225471 , 11111111111111111111111111111101)

    def test_reverseBits_one_in_lsb(self):
        self._assert_reverseBits(2**31, 1)

    def test_reverseBits_one_in_msb(self):
        self._assert_reverseBits(1, 10000000000000000000000000000000)

    def test_reverseBits_max_value(self):
        self._assert_reverseBits(2**32 - 1, 11111111111111111111111111111111)

    def _assert_reverseBits(self, expected: int, n: int) -> None:
        actual = self.solution.reverseBits(n)

        self.assertEqual(expected, actual)
