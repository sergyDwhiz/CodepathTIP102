# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

# Example
# Input: nums = [3, 0, 1]
# Output: 2

def missingNumber(nums):
    sum1 = 0
    sum = len(nums) * (len(nums) + 1) // 2
    for i in range(len(nums)):
        sum1 += nums[i]
    return sum - sum1
