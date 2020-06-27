import unittest

from src.perfect_squares.solution import Solution


class TestPerfectSquares(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_numSquares_n_is_a_zero_returns_zero(self):
        self._assert_numSquares(0, 0)

    def test_numSquares_n_is_a_perfect_square_returns_one(self):
        self._assert_numSquares(1, 1)

    def test_numSquares_n_is_a_larger_perfect_square_returns_one(self):
        self._assert_numSquares(1, 25)

    def test_numSquares_n_is_the_sum_of_the_same_perfect_square_returns_two(self):
        self._assert_numSquares(2, 2)

    def test_numSquares_n_is_the_sum_of_only_two_perfect_squares_returns_two(self):
        self._assert_numSquares(2, 5)

    def test_numSquares_n_is_the_sum_of_multiple_permutations_of_perfect_squares_returns_the_least_number(self):
        self._assert_numSquares(2, 13)

    def test_numSquares_least_number_of_squares_does_not_include_largest_square(self):
        self._assert_numSquares(4, 23)

    def test_numSquares_least_number_of_squares_does_not_include_two_largest_squares(self):
        self._assert_numSquares(3, 43)

    def _assert_numSquares(self, expected: int, n: int) -> None:
        actual = self.solution.numSquares(n)

        self.assertEqual(expected, actual)
