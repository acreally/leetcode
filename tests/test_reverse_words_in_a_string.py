import unittest

from src.reverse_words_in_a_string.solution import Solution


class TestReverseWordsInAString(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_reverseWords_empty_string_returns_empty_string(self):
        self._assert_reverseWords('', '')

    def test_reverseWords_no_trailing_or_leading_whitespace_single_space_between_words_alphabetic_characters(self):
        self._assert_reverseWords('the sky is blue', 'blue is sky the')

    def test_reverseWords_no_trailing_or_leading_whitespace_single_space_between_words_numeric_characters(self):
        self._assert_reverseWords('123 45 6789', '6789 45 123')

    def test_reverseWords_no_trailing_or_leading_whitespace_single_space_between_words_special_characters(self):
        self._assert_reverseWords('!@#$ %^ &* ()', '() &* %^ !@#$')

    def test_reverseWords_no_trailing_or_leading_whitespace_single_space_between_words_mixed_characters(self):
        self._assert_reverseWords('$100! won I it? believe you Can', 'Can you believe it? I won $100!')

    def test_reverseWords_leading_whitespace(self):
        self._assert_reverseWords('world! hello', '  hello world!')

    def test_reverseWords_trailing_whitespace(self):
        self._assert_reverseWords('world! hello', 'hello world!    ')

    def test_reverseWords_leading_and_trailing_whitespace(self):
        self._assert_reverseWords('world! hello', '    hello world!    ')

    def test_reverseWords_multiple_spaces_between_words_whitespace(self):
        self._assert_reverseWords('example good a', 'a good   example')

    def _assert_reverseWords(self, expected: str, s: str) -> None:
        actual = self.solution.reverseWords(s)

        self.assertEqual(expected, actual)