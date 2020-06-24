import unittest

from typing import Generic
from src.count_complete_tree_nodes.solution import Solution, TreeNode, TreeNodeObj

class TestCountCompleteTreeNodes(unittest.TestCase, Generic[TreeNode]):

    def setUp(self):
        self.solution = Solution()

    def test_countNodes_root_is_none_returns_zero(self):
        self._assert_countNodes(0, None)

    def test_countNodes_only_root_returns_one(self):
        root = TreeNodeObj()
        self._assert_countNodes(1, root)

    def test_countNodes_root_and_one_child_returns_two(self):
        left = TreeNodeObj()
        root = TreeNodeObj(val=1, left=left)
        self._assert_countNodes(2, root)

    def test_countNodes_root_and_two_child_returns_three(self):
        left = TreeNodeObj(val=0)
        right = TreeNodeObj(val=1)
        root = TreeNodeObj(val=2, left=left, right=right)
        self._assert_countNodes(3, root)

    def test_countNodes_only_left_tree_on_third_level_returns_five(self):
        left_leaf = TreeNodeObj(val=0)
        right_leaf = TreeNodeObj(val=1)
        left = TreeNodeObj(val=2, left=left_leaf, right=right_leaf)
        right = TreeNodeObj(val=3)
        root = TreeNodeObj(val=4, left=left, right=right)
        self._assert_countNodes(5, root)

    def test_countNodes_only_left_tree_on_third_level_returns_six(self):
        right_left = TreeNodeObj(val=0) 
        left_left = TreeNodeObj(val=1)
        left_right = TreeNodeObj(val=2)
        left = TreeNodeObj(val=3, left=left_left, right=left_right)
        right = TreeNodeObj(val=4, left=right_left)
        root = TreeNodeObj(val=5, left=left, right=right)
        self._assert_countNodes(6, root)

    def test_countNodes_full_tree_three_levels_returns_seven(self):
        right_left = TreeNodeObj(val=0)
        right_right = TreeNodeObj(val=1)
        left_left = TreeNodeObj(val=2)
        left_right = TreeNodeObj(val=3)
        left = TreeNodeObj(val=4, left=left_left, right=left_right)
        right = TreeNodeObj(val=5, left=right_left, right=right_right)
        root = TreeNodeObj(val=6, left=left, right=right)
        self._assert_countNodes(7, root)

    def _assert_countNodes(self, expected: int, root: TreeNode) -> None:
        actual = self.solution.countNodes(root)

        self.assertEqual(expected, actual)