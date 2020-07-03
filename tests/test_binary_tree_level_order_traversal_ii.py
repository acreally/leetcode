import unittest

from typing import List

from src.binary_tree_level_order_traversal_ii.solution import Solution, TreeNode

class TestBinaryTreeLevelOrderTraversalII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_levelOrderBottom_none(self):
        self._assert_levelOrderBottom([], None)

    def test_levelOrderBottom_only_root(self):
        self._assert_levelOrderBottom([[1]], TreeNode(1))

    def test_levelOrderBottom_root_and_left_child(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self._assert_levelOrderBottom([[2], [1]], root)

    def test_levelOrderBottom_root_and_right_child(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        self._assert_levelOrderBottom([[3], [1]], root)

    def test_levelOrderBottom_root_and_both_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self._assert_levelOrderBottom([[2, 3], [1]], root)

    def test_levelOrderBottom_left_nodes_only(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self._assert_levelOrderBottom([[4], [3], [2], [1]], root)

    def test_levelOrderBottom_right_nodes_only(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self._assert_levelOrderBottom([[4], [3], [2], [1]], root)

    def test_levelOrderBottom_full_tree_three_levels(self):
        left = TreeNode(2)
        left.left = TreeNode(4)
        left.right = TreeNode(5)
        right = TreeNode(3)
        right.left = TreeNode(6)
        right.right = TreeNode(7)
        root = TreeNode(1)
        root.left = left
        root.right = right
        self._assert_levelOrderBottom([[4, 5, 6, 7], [2, 3], [1]], root)

    def test_levelOrderBottom_three_levels_left_leaves_missing(self):
        left = TreeNode(2)
        right = TreeNode(3)
        right.left = TreeNode(6)
        right.right = TreeNode(7)
        root = TreeNode(1)
        root.left = left
        root.right = right
        self._assert_levelOrderBottom([[6, 7], [2, 3], [1]], root)

    def test_levelOrderBottom_three_levels_right_leaves_missing(self):
        left = TreeNode(2)
        left.left = TreeNode(4)
        left.right = TreeNode(5)
        right = TreeNode(3)
        root = TreeNode(1)
        root.left = left
        root.right = right
        self._assert_levelOrderBottom([[4, 5], [2, 3], [1]], root)

    def test_levelOrderBottom_three_levels_inner_leaves_missing(self):
        left = TreeNode(2)
        left.left = TreeNode(4)
        right = TreeNode(3)
        right.right = TreeNode(7)
        root = TreeNode(1)
        root.left = left
        root.right = right
        self._assert_levelOrderBottom([[4, 7], [2, 3], [1]], root)

    def test_levelOrderBottom_three_levels_outer_leaves_missing(self):
        left = TreeNode(2)
        left.right = TreeNode(5)
        right = TreeNode(3)
        right.left = TreeNode(6)
        root = TreeNode(1)
        root.left = left
        root.right = right
        self._assert_levelOrderBottom([[5, 6], [2, 3], [1]], root)

    def _assert_levelOrderBottom(self, expected: List[List[int]], root: TreeNode) -> None:
        actual = self.solution.levelOrderBottom(root)

        self.assertEqual(expected, actual)