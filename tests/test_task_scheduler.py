import unittest

from typing import List

from src.task_scheduler.solution import Solution


class TestTaskScheduler(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_leastInterval_empty_list_returns_zero(self):
        self._assert_leastInterval(0, [], 0)

    def test_leastInterval_cooldown_is_zero_returns_length_of_list(self):
        self._assert_leastInterval(8, ["A", "A", "A", "B", "B", "B", "B", "C"], 0)

    def test_leastInterval_cooldown_is_one_single_task_returns_number_of_tasks_times_two_minus_one(self):
        self._assert_leastInterval(5, ["A", "A", "A"], 1)

    def test_leastInterval_cooldown_is_one_multiple_tasks_same_frequency_returns_number_of_tasks(self):
        self._assert_leastInterval(4, ["A", "A", "B", "B"], 1)

    def test_leastInterval_cooldown_is_one_highest_frequency_task_has_as_many_jobs_as_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(8, ["A", "A", "A", "B", "B", "B", "B", "C"], 1)

    def test_leastInterval_cooldown_is_one_highest_frequency_task_has_fewer_jobs_than_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(9, ["A", "A", "A", "B", "B", "B", "B", "C", "C"], 1)

    def test_leastInterval_cooldown_is_one_highest_frequency_task_has_more_jobs_as_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(7, ["A", "A", "B", "B", "B", "B", "C"], 1)

    def test_leastInterval_cooldown_is_one_multiple_highest_frequency_tasks_have_as_many_jobs_as_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(12, ["A", "A", "A", "B", "B", "B", "C", "D", "E", "F", "G", "H"], 1)

    def test_leastInterval_cooldown_is_one_multiple_highest_frequency_tasks_have_fewer_jobs_than_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(13, ["A", "A", "A", "B", "B", "B", "C", "C", "D", "D", "E", "E", "F"], 1)

    def test_leastInterval_cooldown_is_one_multiple_highest_frequency_tasks_have_more_jobs_than_rest_of_tasks_returns_length_of_list(self):
        self._assert_leastInterval(9, ["A", "A", "A", "A", "B", "B", "B", "B", "C"], 1)

    def test_leastInterval_multiple_highest_frequency_tasks_idle_between_sets_of_tasks(self):
        self._assert_leastInterval(8, ["A", "A", "A", "B", "B", "B"], 2)

    def test_leastInterval_multiple_idle_periods(self):
        self._assert_leastInterval(9, ["A", "A", "A", "B", "B", "C"], 3)

    def test_leastInterval_sparse_schedule(self):
        self._assert_leastInterval(49, ["A", "A", "A", "B", "B", "C", "D", "D", "D", "D", "D", "E", "E", "E"], 11)

    def test_leastInterval_long_list_long_cooldown_multiple_highest_frequency_tasks(self):
        self._assert_leastInterval(201904, ["A"] * 2000 + ["B"] * 2000 + ["C"] * 2000 + ["D"] * 2000 + ["E"] * 2000, 100)

    def test_leastInterval_long_list_long_cooldown_single_highest_frequency_task(self):
        self._assert_leastInterval(1009900, ["A"] * 10000, 100)

    def _assert_leastInterval(self, expected: int, tasks: List[str], n: int) -> None:
        actual = self.solution.leastInterval(tasks, n)

        self.assertEqual(expected, actual)
