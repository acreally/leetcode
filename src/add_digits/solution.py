class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num - 9 * ((num - 1) // 9)
