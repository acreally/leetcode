from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations is None:
            return None
        if not citations:
            return 0

        h = min(1, citations[len(citations) - 1])
        for i in range(len(citations) - 2, -1, -1):
            h = max(min(citations[i], len(citations) - i), h)
        return h
