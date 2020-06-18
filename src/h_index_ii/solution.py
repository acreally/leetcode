from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations is None:
            return None
        if not citations:
            return 0

        return self.compute(0, len(citations) - 1, citations)

    def compute(self, start: int, end: int, citations: List[int]) -> int:
        if start == end:
            return min(citations[end], len(citations) - end)
        else:
            mid = (start + end) // 2
            return max(self.compute(start, mid, citations), self.compute(mid + 1, end, citations))
