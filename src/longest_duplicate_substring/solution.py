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
        dup_substrings = set()
        start = 0
        end = current_substring_len
        while (end < len(S) + 1):
            current_substring = S[start: end]
            current_substring_hash = hash(current_substring)
            inner_start = 0
            inner_end = current_substring_len
            while (inner_end < len(S) + 1):
                if inner_start == start and inner_end == end:
                    inner_start += 1
                    inner_end += 1
                    continue
                compare_substring = S[inner_start: inner_end]
                compare_substring_hash = hash(compare_substring)
                if current_substring_hash == compare_substring_hash:
                    if current_substring == compare_substring:
                        dup_substrings.add(current_substring)
                inner_start += 1
                inner_end += 1
            start += 1
            end += 1
        if dup_substrings:
            return dup_substrings.pop()
        return ""