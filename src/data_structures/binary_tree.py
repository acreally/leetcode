from typing import List


class BinaryTreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        result = True
        if not other:
            return False
        if not isinstance(other, BinaryTreeNode):
            return False
        if self.val != other.val:
            return False
        if self.left:
            if not other.left:
                return False
            else:
                result = result and self.left == other.left
        else:
            if other.left:
                return False
        if self.right:
            if not other.right:
                return False
            else:
                result = result and self.right == other.right
        else:
            if other.right:
                return False
        return result

    @staticmethod
    def from_list(vals: List[int]):
        if not vals or len(vals) < 1:
            return None
        nodes = [BinaryTreeNode(val) if val else None for val in vals]
        for i in range(0, len(nodes)):
            if nodes[i]:
                left = BinaryTreeNode.left_child(i)
                if left < len(nodes):
                    nodes[i].left = nodes[left]
                right = BinaryTreeNode.right_child(i)
                if right < len(nodes):
                    nodes[i].right_child = nodes[right]
        return nodes[0]

    @staticmethod
    def parent(index: int) -> int:
        if index % 2 == 0:
            return (index - 1) // 2
        return index // 2

    @staticmethod
    def left_child(index: int) -> int:
        return index * 2 + 1

    @staticmethod
    def right_child(index: int) -> int:
        return index * 2 + 2
