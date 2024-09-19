from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_current = max_global = nums[0]

        if not nums:
            return 0

        # Kadane's algorithm
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            if max_current > max_global:
                max_global = max_current

        return max_global
