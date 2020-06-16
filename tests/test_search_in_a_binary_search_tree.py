import unittest

from typing import Generic, TypeVar

from src.search_in_a_binary_search_tree.solution import Solution, TreeNode


T = TypeVar('TreeNode')


class TestSearchInABinarySearchTree(unittest.TestCase, Generic[T]):

    def setUp(self):
        self.solution = Solution()
        self.root = TreeNode(4)
        self.first_left = TreeNode(2)
        self.first_right = TreeNode(7)
        self.root.left = self.first_left
        self.root.right = self.first_right
        self.second_left = TreeNode(1)
        self.second_right = TreeNode(3)
        self.first_left.left = self.second_left
        self.first_left.right = self.second_right

    def test_next_search_value_is_greater_than_non_leaf_root_returns_right(self):
        self._assert_next(self.first_right, self.root, 6)

    def test_next_search_value_is_less_than_non_leaf_root_returns_left(self):
        self._assert_next(self.first_left, self.root, 2)

    def test_next_search_value_is_greater_than_leaf_root_returns_none(self):
        self._assert_next(None, self.first_right, 9)

    def test_next_search_value_is_less_than_leaf_root_returns_none(self):
        self._assert_next(None, self.first_right, 1)

    def _assert_next(self, expected: TreeNode, root: TreeNode, search_value: int):
        actual = self.solution.get_next(root, search_value)

        self.assertEqual(expected, actual)

    def test_searchBST_value_is_root_returns_root(self):
        self._assert_searchBST(self.root, self.root, 4)

    def test_searchBST_value_is_non_leaf_child_of_root_returns_node(self):
        self._assert_searchBST(self.first_left, self.root, 2)

    def test_searchBST_value_is_leaf_child_of_root_returns_node(self):
        self._assert_searchBST(self.first_right, self.root, 7)

    def test_searchBST_value_is_leaf_grandchild_of_root_returns_node(self):
        self._assert_searchBST(self.second_right, self.root, 3)

    def test_searchBST_value_greater_than_root_not_found_returns_none(self):
        self._assert_searchBST(None, self.root, 5)

    def test_searchBST_value_less_than_root_not_found_returns_none(self):
        self._assert_searchBST(None, self.root, 0)

    def test_searchBST_value_less_than_all_tree_of_decreasing_values_returns_none(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        self._assert_searchBST(None, root, 2)

    def test_searchBST_value_greater_than_all_tree_of_decreasing_values_returns_none(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        self._assert_searchBST(None, root, 6)

    def test_searchBST_value_in_non_leaf_tree_of_decreasing_values_returns_node(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        self._assert_searchBST(root.left, root, 4)

    def test_searchBST_value_in_leaf_tree_of_decreasing_values_returns_node(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        self._assert_searchBST(root.left.left, root, 3)

    def test_searchBST_value_less_than_all_tree_of_increasing_values_not_found_returns_none(self):
        root = TreeNode(3)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self._assert_searchBST(None, root, 2)

    def test_searchBST_value_greater_than_all_tree_of_increasing_values_value_in_non_leaf_returns_none(self):
        root = TreeNode(3)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self._assert_searchBST(None, root, 6)

    def test_searchBST_value_in_non_leaf_tree_of_increasing_values_returns_node(self):
        root = TreeNode(3)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self._assert_searchBST(root.right, root, 4)

    def test_searchBST_value_in_leaf_tree_of_increasing_values_returns_node(self):
        root = TreeNode(3)
        root.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self._assert_searchBST(root.right.right, root, 5)

    def _assert_searchBST(self, expected: TreeNode, root: TreeNode, val: int):
        actual = self.solution.searchBST(root, val)

        self.assertEqual(expected, actual)