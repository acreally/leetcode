

class Node:
    next = None
    prev = None
    child = None

    def __init__(self, val: int):
        self.val = val

class Solution:
    def flatten(self, head: Node) -> Node:
        result = head
        current = head

        while current:
            if current.child:
                current = self.insert_child_list(current, current.child)
            if current:
                current = current.next

        return result

    def insert_child_list(self, parent, child):
        next = parent.next
        current = child
        parent.next = child
        child.prev = parent
        parent.child = None
        while current.next:
            if current.child:
                current = self.insert_child_list(current, current.child)
            if current.next:
                current = current.next

        current.next = next
        if next:
            next.prev = current
        return next