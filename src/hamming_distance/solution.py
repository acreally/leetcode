class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_quotient = x
        y_quotient = y
        result = 0
        while x_quotient > 0 or y_quotient > 0:
            x_remainder = x_quotient % 2
            y_remainder = y_quotient % 2
            if x_remainder != y_remainder:
                result += 1
            x_quotient = x_quotient // 2
            y_quotient = y_quotient // 2
        return result
