from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        output = []

        for number in counter.most_common(k):
            output.append(number[0])

        return output
