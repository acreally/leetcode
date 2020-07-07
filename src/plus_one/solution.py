from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        carry_over = 1
        for i in range(len(digits) - 1, -1, -1):
            current = digits[i] + carry_over
            result.append(current % 10)
            carry_over = current // 10

        if carry_over:
            result += [1]

        result.reverse()

        return result
