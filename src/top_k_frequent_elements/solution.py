from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        if not nums:
            return result

        (counts, max_count) = self.get_counts(nums)
        sorted_counts = self.counting_sort(counts, max_count)
        result = []
        while k > 0:
            result.append(sorted_counts.pop())
            k -= 1

        return result

    def get_counts(self, nums: List[int]) -> List:
        result = {}
        max_count = 0
        for num in nums:
            result[num] = result.get(num, 0) + 1
            max_count = max(result[num], max_count)

        return [item for item in result.items()], max_count

    def counting_sort(self, items: List, max_value: int) -> List[int]:
        result = [0] * len(items)
        counts = [0] * max_value
        for item in items:
            counts[item[1] - 1] += 1
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        for j in range(len(items) - 1, -1, -1):
            result[counts[items[j][1] - 1] - 1] = items[j][0]
            counts[items[j][1] - 1] -= 1
        return result

