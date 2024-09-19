from ast import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_current = min_current = max_global = nums[0]

        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] < 0: # Negative numbers
                max_current, min_current = min_current, max_current

            max_current = max(nums[i], max_current * nums[i])
            min_current = min(nums[i], min_current * nums[i])

            if max_current > max_global:
                max_global = max_current

        return max_global