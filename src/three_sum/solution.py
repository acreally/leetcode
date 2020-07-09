from typing import Dict, List, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums:
            return result

        sums_of_pairs = self.get_sums_of_pairs(nums)
        seen = set()
        for i in range(len(nums)):
            if i in seen:
                continue
            current = nums[i]
            diff = 0 - current
            if diff in sums_of_pairs and sums_of_pairs[diff]:
                pairs = sums_of_pairs[diff]
                put_back = []
                while pairs:
                    pair = pairs.pop()
                    indices = list(pair.keys())
                    if indices[0] in seen:
                        continue
                    if indices[1] in seen:
                        continue
                    if i not in pair:
                        seen.add(i)
                        for index in list(pair.keys()):
                            seen.add(index)
                        result.append([current] + list(pair.values()))
                        break
                    else:
                        put_back.append(pair)
                pairs += put_back

        return result

    def get_sums_of_pairs(self, nums: List[int]) -> Dict[int, List[Dict[int, int]]]:
        result = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum not in result:
                    result[sum] = []
                result[sum].append({i: nums[i], j: nums[j]})

        return result
