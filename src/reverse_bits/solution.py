class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        quotient = n
        for i in range(33):
            mod = quotient % 10
            quotient = quotient // 10
            result += mod * 2**(31 - i)

        return result
