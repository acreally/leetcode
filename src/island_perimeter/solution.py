from typing import List, Set, Tuple

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        if not grid or len(grid) == 0:
            return result

        if not grid[0] or len(grid[0]) == 0:
            return result

        width = len(grid[0])
        height = len(grid)
        first_island_square = self.find_first_island_square(grid, width, height)

        if not first_island_square:
            return result

        to_visit = set([first_island_square])
        seen = set()

        while to_visit:
            current = to_visit.pop()
            seen.add(current)
            x = current[0]
            y = current[1]

            result += self.check_square(grid, to_visit, seen, x - 1, y, x - 1 < 0)
            result += self.check_square(grid, to_visit, seen, x + 1, y, x + 1 >= width)
            result += self.check_square(grid, to_visit, seen, x, y - 1, y - 1 < 0)
            result += self.check_square(grid, to_visit, seen, x, y + 1, y + 1 >= height)

        return result

    def find_first_island_square(self, grid: List[List[int]], width: int, height: int) -> Tuple[int, int]:
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    return (x, y)

    def check_square(self,
                     grid: List[List[int]],
                     to_visit: Set[Tuple[int, int]],
                     seen: Set[Tuple[int, int]],
                     x: int,
                     y: int,
                     comparison: bool) -> int:
        if (x, y) in seen:
            return 0

        if comparison:
            return 1
        else:
            if grid[y][x] == 0:
                return 1
            to_visit.add((x, y))
            return 0
