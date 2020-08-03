import unittest

from src.valid_palindrome.solution import Solution


class TestValidPalindrome(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_isPalindrome_empty_string_returns_true(self):
        self._assert_isPalindrome(True, '')

    def test_isPalindrome_single_alpha_character_returns_true(self):
        self._assert_isPalindrome(True, 'a')
    
    def test_isPalindrome_single_numeric_character_returns_true(self):
        self._assert_isPalindrome(True, '1')

    def test_isPalindrome_single_space_character_returns_true(self):
        self._assert_isPalindrome(True, ' ')

    def test_isPalindrome_even_number_of_space_characters_returns_true(self):
        self._assert_isPalindrome(True, '    ')

    def test_isPalindrome_single_special_character_returns_true(self):
        self._assert_isPalindrome(True, '.')

    def test_isPalindrome_multiple_special_characters_returns_true(self):
        self._assert_isPalindrome(True, '.,!@#$')

    def test_isPalindrome_only_alphanumeric_lower_case_odd_length_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '1racecar1')

    def test_isPalindrome_only_alphanumeric_lower_case_even_length_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '2raceecar2')

    def test_isPalindrome_only_alphanumeric_lower_case_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, '1racecars')

    def test_isPalindrome_only_alpha_upper_case_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, 'RACECAR')

    def test_isPalindrome_only_alpha_upper_case_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, 'RACECARS')

    def test_isPalindrome_only_alpha_mixed_case_not_matching_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, 'RAcECAr')

    def test_isPalindrome_only_alpha_mixed_case_not_matching_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, 'RAcECaRS')

    def test_isPalindrome_alphanumeric_with_spaces_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '1 race car1')

    def test_isPalindrome_alphanumeric_with_spaces_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, '1 rae car1')

    def test_isPalindrome_alphanumeric_leading_and_trailing_whitespace_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '   1racecar1  ')

    def test_isPalindrome_alphanumeric_leading_whitespace_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '   1racecar1')

    def test_isPalindrome_alphanumeric_trailing_whitespace_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, '1racecar1  ')

    def test_isPalindrome_alphanumeric_with_spaces_and_special_chars_mixed_case_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, 'A man, a plan, a canal: Panama')

    def test_isPalindrome_alphanumeric_with_spaces_and_special_chars_mixed_case_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, 'A man, a plan, canal: Panama')

    def test_isPalindrome_long_word_is_palindrome_returns_true(self):
        self._assert_isPalindrome(True, 'a' * 10000000)

    def test_isPalindrome_long_word_is_not_palindrome_returns_false(self):
        self._assert_isPalindrome(False, 'a' * 5000000 + 'b' + 'a' * 4999999)

    def _assert_isPalindrome(self, expected: bool, s: str) -> None:
        actual = self.solution.isPalindrome(s)

        self.assertEqual(expected, actual)
