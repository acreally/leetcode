import unittest

from typing import List

from src.course_schedule_ii.solution import Solution


class TestCourseScheduleII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_findOrder_no_prereqs_returns_all_courses(self):
        self._assert_findOrder([0, 1, 2], 3, [])

    def test_findOrder_one_prereq_for_all_but_one_course(self):
        self._assert_findOrder([0, 1, 2, 3], 4, [[1, 0], [2, 1], [3, 2]])

    def test_findOrder_multiple_prereqs_for_a_course(self):
        self._assert_findOrder([2, 3, 0, 1], 4, [[1, 0], [1, 3], [3, 2]])

    def test_findOrder_cycle_in_prereqs_returns_empty_list(self):
        self._assert_findOrder([], 4, [[1, 0], [2, 1], [3, 2], [0, 3]])

    def _assert_findOrder(self, expected: List[int], numCourses: int, prerequisites: List[List[int]]) -> None:
        actual = self.solution.findOrder(numCourses, prerequisites)

        self.assertEqual(len(expected), len(actual))
        for course in expected:
            self.assertTrue(course in actual)
