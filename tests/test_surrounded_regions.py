import unittest

from src.surrounded_regions.solution import Solution


class TestSurroundedRegions(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_solve_board_is_none(self):
        self._assert_solve(None, None)

    def test_solve_board_is_empty(self):
        self._assert_solve([], [])

    def test_solve_board_contains_empty_lists(self):
        self._assert_solve([[],[],[]], [[],[],[]])

    def test_solve_surrounded_region_with_o_on_border_flips_region(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

        self._assert_solve(expected, board)

    def test_solve_one_o_surrounded_gets_flipped(self):
        board = [["O","O","X","O"],["O","X","O","X"],["O","O","X","O"],["O","O","O","O"]]
        expected = [["O","O","X","O"],["O","X","X","X"],["O","O","X","O"],["O","O","O","O"]]

        self._assert_solve(expected, board)

    def test_solve_no_surrounded_region_with_os_on_border_nothing_flips(self):
        board = [["X","X","O","X"],["X","X","X","X"],["X","X","X","O"],["X","O","X","X"]]
        expected = [["X","X","O","X"],["X","X","X","X"],["X","X","X","O"],["X","O","X","X"]]

        self._assert_solve(expected, board)

    def test_solve_only_corners_are_os_nothing_flips(self):
        board = [["O","X","X","O"],["X","X","X","X"],["X","X","X","X"],["O","X","X","O"]]
        expected = [["O","X","X","O"],["X","X","X","X"],["X","X","X","X"],["O","X","X","O"]]

        self._assert_solve(expected, board)

    def test_solve_corners_and_middle_are_os_flips_middle(self):
        board = [["O","X","X","O"],["X","O","O","X"],["X","O","O","X"],["O","X","X","O"]]
        expected = [["O","X","X","O"],["X","X","X","X"],["X","X","X","X"],["O","X","X","O"]]

        self._assert_solve(expected, board)

    def test_solve_surrounded_region_except_for_border_nothing_flips(self):
        board = [["X","O","O","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]]
        expected = [["X","O","O","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]]

        self._assert_solve(expected, board)

    def test_solve_xs_on_border_os_in_middle_flips_middle(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]

        self._assert_solve(expected, board)

    def test_solve_os_on_border_xs_in_middle_flips_nothing(self):
        board = [["O","O","O","O"],["O","X","X","O"],["O","X","X","O"],["O","O","O","O"]]
        expected = [["O","O","O","O"],["O","X","X","O"],["O","X","X","O"],["O","O","O","O"]]

        self._assert_solve(expected, board)

    def test_solve_multiple_surrounded_regions_sharing_border_get_flipped(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","O","O","X"],["X","X","X","X"]]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]

        self._assert_solve(expected, board)

    def test_solve_multiple_surrounded_regions_not_sharing_border_get_flipped(self):
        board = [["X","X","X","X"],["X","O","O","X"],["X","X","X","X"],["X","X","X","X"],["X","O","O","X"],["X","X","X","X"]]
        expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]

        self._assert_solve(expected, board)

    def _assert_solve(self, expected, board):
        self.solution.solve(board)

        self.assertEqual(expected, board)
