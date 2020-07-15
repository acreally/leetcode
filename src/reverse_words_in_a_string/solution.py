class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s

        words = [word for word in s.strip().split(' ') if word]
        words.reverse()
        return ' '.join(words)
