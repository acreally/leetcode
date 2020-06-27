from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0

        squares = self.get_squares(n)

        least_number_of_squares = None
        for i in range(len(squares) - 1, -1, -1):
            sum, number_of_squares = self.find_sum(n, squares, i)
            if sum == n:
                if not least_number_of_squares or number_of_squares < least_number_of_squares:
                    least_number_of_squares = number_of_squares

        return least_number_of_squares

    def get_squares(self, n: int) -> List[int]:
        squares = []
        
        for i in range(1, n + 1):
            current_square = i**2
            if current_square <= n:
                squares.append(current_square)

        return squares

    def find_sum(self, n: int, squares: List[int], start: int) -> (int, int):
        sum = 0
        number_of_squares = 0
        i = start
        while i >= 0:
            sum += squares[i]
            if sum == n:
                number_of_squares += 1
                break
            elif sum < n:
                number_of_squares += 1
                i += 1
            else:
                sum -= squares[i]
            i -= 1

        return sum, number_of_squares
