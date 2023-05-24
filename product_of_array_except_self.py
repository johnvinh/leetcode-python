from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        # same length as input
        answer = [0] * length

        # answer[i] contains the product of all the numbers to the left of i
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        right_product = 1

        for i in reversed(range(length)):
            answer[i] = answer[i] * right_product
            right_product *= nums[i]

        return answer
