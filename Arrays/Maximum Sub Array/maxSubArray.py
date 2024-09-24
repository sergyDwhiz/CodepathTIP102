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

# OR
def find_max_sum_sublist(nums):
    if len(nums) < 1:
        return 0

    curr_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        if curr_max < 0:
            curr_max = nums[i]
        else:
            curr_max += nums[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max