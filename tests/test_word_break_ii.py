import unittest

from typing import List

from src.word_break_ii.solution import Solution


class TestWordBreakII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_wordBreak_extra_letter_at_the_start_no_matches(self):
        self._assert_wordBreak([], "xcatsanddog", ["cats", "and", "dog"])

    def test_wordBreak_extra_letter_in_the_midle_between_words_no_matches(self):
        self._assert_wordBreak([], "catsxanddog", ["cats", "and", "dog"])

    def test_wordBreak_extra_letter_in_the_midle_in_a_word_no_matches(self):
        self._assert_wordBreak([], "catsaxnddog", ["cats", "and", "dog"])

    def test_wordBreak_extra_letter_at_the_end_no_matches(self):
        self._assert_wordBreak([], "catsanddogx", ["cats", "and", "dog"])

    def test_wordBreak_single_answer_starts_with_shortest_word(self):
        self._assert_wordBreak(["and cats doggos"], "andcatsdoggos", ["cats", "and", "doggos"])

    def test_wordBreak_single_answer_starts_with_middle_length_word(self):
        self._assert_wordBreak(["cats and doggos"], "catsanddoggos", ["cats", "and", "doggos"])

    def test_wordBreak_single_answer_starts_with_longest_word(self):
        self._assert_wordBreak(["doggos and cats"], "doggosandcats", ["cats", "and", "doggos"])

    def test_wordBreak_single_answer_extra_dictionary_word_no_overlap_at_start(self):
        self._assert_wordBreak(["cats and dog"], "catsanddog", ["cats", "and", "dog", "cat"])

    def test_wordBreak_single_answer_extra_dictionary_word_no_overlap_in_middle(self):
        self._assert_wordBreak(["cats and dog"], "catsanddog", ["cats", "and", "dog", "sand"])

    def test_wordBreak_single_answer_extra_dictionary_word_no_overlap_at_end(self):
        self._assert_wordBreak(["cats and dog"], "catsanddog", ["cats", "and", "dog", "ddog"])

    def test_wordBreak_single_answer_extra_dictionary_word_overlap(self):
        self._assert_wordBreak(["cats and dog"], "catsanddog", ["cats", "and", "dog", "sand"])

    def test_wordBreak_all_the_same_word_matches(self):
        self._assert_wordBreak(["cat cat cat"], "catcatcat", ["cat", "and", "dog", "sand"])

    def test_wordBreak_two_answers(self):
        self._assert_wordBreak(["cats and dog", "cat sand dog"], "catsanddog", ["cat", "cats", "and", "sand", "dog"])

    def test_wordBreak_three_answers(self):
        self._assert_wordBreak(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"], "pineapplepenapple",
                               ["apple", "pen", "applepen", "pine", "pineapple"])

    def test_wordBreak_lots_of_overlapping_words_no_matches(self):
        self._assert_wordBreak([],
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
                               ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
                              )

    def _assert_wordBreak(self, expected: List[str], s: str, wordDict: List[str]) -> None:
        actual = self.solution.wordBreak(s, wordDict)

        self.assertEqual(set(expected), set(actual))
