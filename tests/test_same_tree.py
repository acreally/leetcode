import unittest

from src.data_structures.binary_tree import BinaryTreeNode as TreeNode
from src.same_tree.solution import Solution


class TestSameTree(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_isSameTree_both_none_returns_true(self):
        self._assert_isSameTree(True, None, None)

    def test_isSameTree_one_node_same_values_returns_true(self):
        self._assert_isSameTree(True, TreeNode(12), TreeNode(12))

    def test_isSameTree_one_node_different_values_returns_false(self):
        self._assert_isSameTree(False, TreeNode(12), TreeNode(21))

    def test_isSameTree_multiple_nodes_same_values_same_structure_returns_true(self):
        self._assert_isSameTree(True, TreeNode.from_list([1, 2, 3, None, 4, 5, None, None, 6]),
            TreeNode.from_list([1, 2, 3, None, 4, 5, None, None, 6]))

    def test_isSameTree_multiple_nodes_different_values_same_structure_returns_false(self):
        self._assert_isSameTree(False, TreeNode.from_list([11, 21, 33, None, 433, 522, None, None, 126]),
            TreeNode.from_list([1, 2, 3, None, 4, 5, None, None, 6]))

    def test_isSameTree_multiple_nodes_same_values_different_structure_returns_false(self):
        self._assert_isSameTree(False, TreeNode.from_list([1, 2, 3, None, 4, 5, None, None, 6]),
            TreeNode.from_list([1, 2, 3, 4, 5, 6]))

    def _assert_isSameTree(self, expected: bool, p: TreeNode, q: TreeNode) -> None:
        actual = self.solution.isSameTree(p, q)

        self.assertEqual(expected, actual)
