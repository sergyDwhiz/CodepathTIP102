from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero_found_at = 0

        for current in range(len(nums)):
            if nums[current] != 0:
                nums[last_non_zero_found_at] = nums[current]
                last_non_zero_found_at += 1

        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
