import unittest

from src.flatten_a_multilevel_doubly_linked_list.solution import Node, Solution


class TestFlattenADoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_flatten_none_returns_none(self):
        self._assert_flatten(None, None)

    def test_flatten_no_children(self):
        tail = Node(3)
        mid = Node(2)
        head = Node(1)
        
        head.next = mid
        mid.next = tail
        mid.prev = head
        tail.prev = mid
        self._assert_flatten(head, head)

    def test_flatten_head_has_child(self):
        child_head = Node(4)
        child_tail = Node(5)
        tail = Node(3)
        mid = Node(2)
        head = Node(1)
        
        head.next = mid
        head.child = child_head
        child_head.next = child_tail
        child_tail.prev = child_head
        mid.next = tail
        mid.prev = head
        tail.prev = mid

        expected = Node(1)
        expected.next = Node(4)
        expected.next.prev = expected
        expected.next.next = Node(5)
        expected.next.next.prev = expected.next
        expected.next.next.next = Node(2)
        expected.next.next.next.prev = expected.next.next
        expected.next.next.next.next = Node(3)
        expected.next.next.next.next.prev = expected.next.next.next

        self._assert_flatten(expected, head)

    def test_flatten_nested_child_lists(self):
        child_head = Node(4)
        child_tail = Node(5)
        child_child_head = Node(6)
        child_child_tail = Node(7)
        tail = Node(2)
        head = Node(1)
        
        head.next = tail
        head.child = child_head
        child_head.child = child_child_head
        child_child_head.next = child_child_tail
        child_child_tail.prev = child_child_head
        child_head.next = child_tail
        child_tail.prev = child_head
        tail.prev = head

        expected = Node(1)
        expected.next = Node(4)
        expected.next.prev = expected
        expected.next.next = Node(6)
        expected.next.next.prev = expected.next
        expected.next.next.next = Node(7)
        expected.next.next.next.prev = expected.next.next
        expected.next.next.next.next = Node(5)
        expected.next.next.next.next.prev = expected.next.next.next
        expected.next.next.next.next.next = Node(2)
        expected.next.next.next.next.next.prev = expected.next.next.next.next

        self._assert_flatten(expected, head)

    def _assert_flatten(self, expected: Node, head: Node) -> None:
        actual = self.solution.flatten(head)

        if expected is None:
            self.assertIsNone(actual)
        current_expected = expected
        current_actual = actual
        last_expected = None
        last_actual = None
        while(current_expected):
            self.assertIsNotNone(current_actual)
            self.assertEqual(current_expected.val, current_actual.val)
            last_expected = current_expected
            last_actual = current_actual
            current_actual = current_actual.next
            current_expected = current_expected.next

        self.assertEqual(None, current_actual)

        current_expected = last_expected
        current_actual = last_actual

        while(current_expected):
            self.assertIsNotNone(current_actual)
            self.assertEqual(current_expected.val, current_actual.val)
            current_actual = current_actual.prev
            current_expected = current_expected.prev

        self.assertEqual(None, current_actual)


