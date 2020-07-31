import sys

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hashes, max_len, min_len = self.get_hashes(wordDict)
        candidates = [("", 0)]
        result = []

        while candidates:
            current_candidate = candidates.pop()
            prefix = current_candidate[0]
            start = current_candidate[1]
            if start > len(s) - 1:
                result.append(current_candidate[0].strip())
                continue
            end = start + min_len
            while end - start <= max_len and end <= len(s):
                current_word = s[start:end]
                current_hash = hash(current_word)
                if current_hash in hashes:
                    if current_word in hashes[current_hash]:
                        candidates.append((prefix + " " + current_word, end))
                end += 1

        return result

    def get_hashes(self, wordDict: List[str]) -> dict:
        min_len = sys.maxsize
        max_len = 0
        hashes = {}

        for word in wordDict:
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))
            word_hash = hash(word)
            hash_list = hashes.get(word_hash, [])
            hash_list.append(word)
            hashes[word_hash] = hash_list

        return hashes, max_len, min_len
