from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        return self.get_values([root])

    def get_values(self, to_visit: List[TreeNode]) -> List[List[int]]:
        current_level = 0
        to_next_level = 1
        next_to_next_level = 0
        result = []
        while to_visit:
            while to_next_level > 0:
                current = to_visit.pop(0)
                if len(result) < current_level + 1:
                    result.append([])
                result[current_level].append(current.val)
                if current.left:
                    to_visit.append(current.left)
                    next_to_next_level += 1
                if current.right:
                    to_visit.append(current.right)
                    next_to_next_level += 1
                to_next_level -= 1
            current_level += 1
            to_next_level = next_to_next_level
            next_to_next_level = 0
        result.reverse()
        return result
