from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # lol
        return [int(num) for num in str(int(''.join([str(digit) for digit in digits])) + 1)]