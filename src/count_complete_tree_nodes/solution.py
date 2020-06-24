from typing import TypeVar, Generic

TreeNode = TypeVar('TreeNodeObj')

class Solution(Generic[TreeNode]):
    def countNodes(self, root: TreeNode) -> int:
        to_check = []
        if root:
            to_check.append(root)
        result = 0
        while to_check:
            result += 1
            current = to_check.pop()
            if current.left:
                to_check.append(current.left)
            if current.right:
                to_check.append(current.right)

        return result

class TreeNodeObj:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
