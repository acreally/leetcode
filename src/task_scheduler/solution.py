from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        if n == 0:
            return len(tasks)
        max_freq, num_max_freq = self.find_max_frequency(tasks)
        result = max_freq * (n + 1) - n + (num_max_freq - 1)
        if result < len(tasks):
            return len(tasks)
        return result

    def find_max_frequency(self, tasks: List[str]) -> (int, int):
        max_freq = 0
        num_max_freq = 0
        counts = {}
        for task in tasks:
            count = counts.get(task, 0) + 1
            counts[task] = count
            if count > max_freq:
                max_freq = count
                num_max_freq = 1
            elif count == max_freq:
                num_max_freq += 1
        return max_freq, num_max_freq
