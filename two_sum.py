from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, number in enumerate(nums):
            if number in complements:
                return [i, complements[number]]
            complements[target - number] = i
