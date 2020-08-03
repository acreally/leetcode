class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = True

        s = s.strip()
        if len(s) == 0:
            return result

        start = 0
        end = len(s) - 1
        while start <= end:
            first_token, start = self.get_next_token(s, start)
            second_token, end = self.get_previous_token(s, end)

            first_token = first_token.lower()
            second_token = second_token.lower()

            if first_token != second_token:
                return False

            start += 1
            end -= 1

        return result

    def get_next_token(self, s: str, current_index: int) -> str:
        token = s[current_index]
        while current_index < len(s) - 1 and not token.isalnum():
            current_index += 1
            token = s[current_index]

        if current_index == len(s) - 1 and not token.isalnum():
            token = ''
        return token, current_index

    def get_previous_token(self, s: str, current_index: int) -> str:
        token = s[current_index]
        while current_index > 0 and not token.isalnum():
            current_index -= 1
            token = s[current_index]

        if current_index == 0 and not token.isalnum():
            token = ''
        return token, current_index
