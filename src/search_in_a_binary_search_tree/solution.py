from typing import Generic, TypeVar

T = TypeVar('TreeNode')


class TreeNode(Generic[T]):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        if isinstance(other, TreeNode):
            if self.val != other.val:
                return False
            if self.left != other.left:
                return False
            if self.right != other.right:
                return False
            return True
        return False

    def __repr__(self):
        return "val: {}, left: {}, right: {}".format(self.val, self.left, self.right)

class Solution(Generic[T]):
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        current = root
        while current != None and current.val != val:
            current = self.get_next(current, val)

        return current

    def get_next(self, node: TreeNode, search_value: int) -> TreeNode:
        if search_value < node.val:
            return node.left
        elif search_value > node.val:
            return node.right

        return None

