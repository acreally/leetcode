import sys


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x

        abs_x = abs(x)
        abs_n = abs(n)

        negative_multiplier = 1
        if x < 0 and abs_n % 2 == 1:
            negative_multiplier = -1

        if abs_x == 0 or abs_x == 1:
            return abs_x * negative_multiplier

        invert = n < 0

        result = abs_x

        limit = sys.float_info.max / abs_x
        counter = 1
        while result <= limit and result > 0 and counter < abs_n:
            result *= abs_x
            counter += 1

        if counter < abs_n:
            if result > abs_x:
                if invert:
                    return 0
                return float('inf') * negative_multiplier
            else:
                if invert:
                    return float('inf') * negative_multiplier
                return 0

        if invert:
            result = 1/result

        return result * negative_multiplier
