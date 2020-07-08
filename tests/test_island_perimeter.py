import unittest

from typing import List

from src.island_perimeter.solution import Solution

class TestIslandPerimeter(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_islandPerimeter_empty_list_returns_zero(self):
        self._assert_islandPerimeter(0, [])

    def test_islandPerimeter_list_with_empty_list_returns_zero(self):
        self._assert_islandPerimeter(0, [[]])

    def test_islandPerimeter_no_island_returns_zero(self):
        self._assert_islandPerimeter(0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_islandPerimeter_whole_grid_is_island_returns_perimeter_of_grid(self):
        self._assert_islandPerimeter(12, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    def test_islandPerimeter_island_not_on_boundary_returns_perimeter_of_island(self):
        self._assert_islandPerimeter(8 , [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])

    def test_islandPerimeter_island_has_parts_on_boundary_returns_perimeter_of_island(self):
        self._assert_islandPerimeter(16 , [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])

    def test_islandPerimeter_island_is_bottom_row_returns_perimeter_of_island(self):
        self._assert_islandPerimeter(10, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]])

    def test_islandPerimeter_island_is_a_single_square_returns_perimeter_of_a_square(self):
        self._assert_islandPerimeter(4, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])

    def _assert_islandPerimeter(self, expected: int, grid: List[List[int]]) -> None:
        actual = self.solution.islandPerimeter(grid)

        self.assertEqual(expected, actual)