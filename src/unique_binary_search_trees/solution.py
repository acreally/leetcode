class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        cache = {0: 1, 1: 1}
        return self.compute(n, cache)

    def compute(self, n: int, cache):
        if n in cache:
            return cache[n]
        level = n // 2
        left_subtrees = 0
        right_subtrees = n - 1
        odd = n % 2 == 1
        result = 0
        while level > 0:
            result += 2 * self.compute(right_subtrees, cache) * self.compute(left_subtrees, cache)
            left_subtrees += 1
            right_subtrees -= 1
            level -= 1

        if odd:
            result += self.compute(right_subtrees, cache)**2

        cache[n] = result
        return result
