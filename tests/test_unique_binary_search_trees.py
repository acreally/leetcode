import unittest

from src.unique_binary_search_trees.solution import Solution


class TestUniqueBinarySearchTrees(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_numTrees_zero_nodes_returns_one(self):
        self._assert_numTrees(1, 0)

    def test_numTrees_one_node_returns_one(self):
        self._assert_numTrees(1, 1) # 1 = f(n-1)^2

    def test_numTrees_two_nodes_returns_two(self):
        self._assert_numTrees(2, 2) # 1 + 1 = 2f(0)f(n-1)

    def test_numTrees_three_nodes_returns_five(self):
        self._assert_numTrees(5, 3) # 2 + 1^2 + 2 = 2f(0)f(n-1) + f(n-2)^2

    def test_numTrees_four_nodes_returns_fourteen(self):
        self._assert_numTrees(14, 4) # 5 + 2 + 2 + 5 = 2f(0)f(n-1) + 2f(1)f(n-2)

    def test_numTrees_five_nodes_returns_forty_two(self):
        self._assert_numTrees(42, 5) # 14 + 5 + 2^2 + 5 + 14 = 2f(0)f(n-1) + 2f(1)f(n-2) + f(n-3)^2

    def test_numTrees_six_nodes_returns_one_hundred_thirty_two(self):
        self._assert_numTrees(132, 6) # 42 + 14 + 2 x 5 + 2 x 5 + 14 + 42 = 2f(0)f(n-1) + 2f(1)f(n-2) + 2f(2)f(n-3)

    def test_numTrees_seven_nodes_returns_four_hundred_twenty_nine(self):
        self._assert_numTrees(429, 7) # 132 + 42 + 2 x 14 + 5^2 + 2 x 14 + 42 + 132 = 2f(0)f(n-1) + 2f(1)f(n-2) + 2f(2)f(n-3) + f(n-4)^2

    def test_numTrees_eight_nodes_returns_one_thousand_four_hundred_thirty(self):
        self._assert_numTrees(1430, 8) # 429 + 132 + 2 x 42 + 5 x 14 + 5 x 14 + 2 x 42 + 132 + 429 = 2f(0)f(n-1) + 2f(1)f(n-2) + 2(f2)f(n-3) + 2(f3)f(n-4)

    def _assert_numTrees(self, expected: int, n: int) -> None:
        actual = self.solution.numTrees(n)

        self.assertEqual(expected, actual)
