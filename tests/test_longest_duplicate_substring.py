import unittest

from src.longest_duplicate_substring.solution import Solution


class TestLongestDuplicateSubstring(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_two_char_string_different_chars_returns_empty(self):
        self._assert_longestDupSubstring("", "ab")

    def test_two_char_string_same_chars_returns_the_char(self):
        self._assert_longestDupSubstring("a", "aa")

    def test_three_char_string_all_different_chars_returns_empty(self):
        self._assert_longestDupSubstring("", "abc")

    def test_three_char_string_first_two_chars_are_the_same_returns_the_char(self):
        self._assert_longestDupSubstring("a", "aac")

    def test_three_char_string_first_and_last_chars_are_the_same_returns_the_char(self):
        self._assert_longestDupSubstring("a", "aba")

    def test_three_char_string_all_chars_are_the_same_returns_the_char_twice(self):
        self._assert_longestDupSubstring("aa", "aaa")

    def test_matching_substrings_overlap(self):
        self._assert_longestDupSubstring("ana", "banana")

    def test_matching_substrings_next_to_each_other_do_not_overlap(self):
        self._assert_longestDupSubstring("ana", "banaana")

    def test_matching_substrings_not_next_to_each_other(self):
        self._assert_longestDupSubstring("ana", "banaefgana")

    def test_multiple_duplicate_substrings_returns_longest(self):
        self._assert_longestDupSubstring("aabbbcccc", "aabbbccccasdfghjklaabbbcccc")

    def test_no_duplicate_substrings_returns_empty(self):
        self._assert_longestDupSubstring("", "0123456789")

    def test_long_string_short_duplicate_substring_returns_substring(self):
        actual = self.solution.longestDupSubstring("moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkqgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc")

        self.assertEqual(4, len(actual))

    def _assert_longestDupSubstring(self, expected: str, S: str) -> None:
        actual = self.solution.longestDupSubstring(S)

        self.assertEqual(expected, actual)
