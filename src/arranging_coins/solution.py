class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return n

        level = 0
        coins_left = n

        while coins_left >= level + 1:
            coins_left -= level + 1
            level += 1

        return level
