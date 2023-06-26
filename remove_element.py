from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        different = []
        for num in nums:
            if num != val:
                different.append(num)
        nums[:len(different)] = different
        return len(different)