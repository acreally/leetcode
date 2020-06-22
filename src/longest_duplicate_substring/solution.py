class Solution:
    def longestDupSubstring(self, S: str) -> str:
        min_substring_len = 0
        max_substring_len = len(S) // 2 + 1
        current_substring_len = (max_substring_len - min_substring_len) // 2
        result = ""
        while min_substring_len < current_substring_len <= max_substring_len:
            longest_substring = self.findDupSubdtring(S, current_substring_len)
            if longest_substring:
                result = longest_substring
                min_substring_len = current_substring_len
                current_substring_len += max((max_substring_len - current_substring_len) // 2, 1)
            else:
                max_substring_len = current_substring_len
                current_substring_len -= max((current_substring_len - min_substring_len) // 2, 1)

        return result

    def findDupSubdtring(self, S: str, current_substring_len: int) -> str:
        hashes = {}
        start = 0
        end = current_substring_len
        while (end < len(S) + 1):
            current_substring = S[start: end]
            if current_substring not in hashes:
                hashes[current_substring]  = 0
            hashes[current_substring] += 1
            start += 1
            end += 1
        pruned_hashes = {k: v for k, v in hashes.items() if v > 1}
        if pruned_hashes:
            return pruned_hashes.popitem()[0]
        return ""
