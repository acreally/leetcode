class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a

        max_num = [bit for bit in a] if len(a) > len(b) else [bit for bit in b]
        min_num = [bit for bit in a] if len(a) <= len(b) else [bit for bit in b]
        overflow = False
        for i in range(len(min_num)):
            min_num_lsb = min_num[len(min_num) - 1 - i]
            overflow = self.add_one(max_num, min_num_lsb, len(max_num) - 1 - i, overflow)

        result = ''.join(max_num)
        if overflow:
            return '1' + result
        return result

    def add_one(self, num: str, addition: str, starting_index: int, overflow: bool) -> bool:
        to_add = addition
        current_index = starting_index
        while to_add == '1' and current_index >= 0:
            lsb = num[current_index]
            if lsb == '0':
                to_add = '0'
                num[current_index] = '1'
            else:
                num[current_index] = '0'
            current_index -= 1
        return overflow or to_add == '1'
