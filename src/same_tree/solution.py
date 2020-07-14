from src.data_structures.binary_tree import BinaryTreeNode as TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return p == q
