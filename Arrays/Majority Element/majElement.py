from typing import List
import typing
class Solution:
    def majorityElement(self, nums: typing.List[int]) -> int:
        majority_candidate = None
        vote_count = 0

        for element in nums:
            if vote_count == 0:
                majority_candidate = element
            vote_count += (1 if element == majority_candidate else -1)

        return majority_candidate
