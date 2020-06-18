import time

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0 or not board[0] or len(board[0]) == 0:
            return
        x = len(board[0])
        y = len(board)

        seen = set()
        for current_y in range(1, y-1):
            for current_x in range(1, x-1):
                if board[current_y][current_x] == 'O' and (current_x, current_y) not in seen:
                    seen.add((current_x, current_y))
                    region = self.search(board, current_x, current_y, x-1, y-1, seen)
                    for point in region:
                        board[point[1]][point[0]] = 'X'

    def search(self, board: List[List[str]], given_x: int, given_y: int, max_x: int, max_y: int, seen) -> List:
        in_region = []
        to_check = [(given_x, given_y)]
        while to_check:
            current = to_check.pop()
            in_region.append((current[0], current[1]))
            seen.add((current[0], current[1]))
            if current[0] <= 0 or current[0] >= max_x or current[1] <= 0 or current[1] >= max_y:
                return []
            if board[current[1]][current[0] - 1] == 'O':
                self.update_to_check((current[0] - 1, current[1]), in_region, to_check)
            if board[current[1]][current[0] + 1] == 'O':
                self.update_to_check((current[0] + 1, current[1]), in_region, to_check)
            if board[current[1] - 1][current[0]] == 'O':
                self.update_to_check((current[0], current[1] - 1), in_region, to_check)
            if board[current[1] + 1][current[0]] == 'O':
                self.update_to_check((current[0], current[1] + 1), in_region, to_check)

        return in_region

    def update_to_check(self, coords, in_region: List, to_check: List) -> None:
        if coords not in in_region:
            to_check.append(coords)

if __name__ == '__main__':
    l0 = ["X", "O", "O", "X", "O", "O", "O"]
    l1 = ["X", "X", "O", "O", "O", "O", "X"]
    l2 = ["X", "O", "O", "O", "O", "O", "X"]
    l3 = ["X", "O", "O", "O", "X", "O", "X"]
    l4 = ["O", "O", "O", "O", "O", "O", "O"]
    template = [l0, l1, l2, l3, l4]
    board = [l * 1000 for l in template * 10]

    solution = Solution()
    start = time.time()
    solution.solve(board)
    end = time.time()
    print(board)
    print("Duration: {}".format(end - start))