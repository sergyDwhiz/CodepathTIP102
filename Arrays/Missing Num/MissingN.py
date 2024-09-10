# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.

# Example
# Input: nums = [3, 0, 1]
# Output: 2

def missingNumber(nums):
    expected_sum = len(nums) * (len(nums) + 1) // 2 # n*(n+1)//2 - sum of first n natural numbers
    actual_sum = sum(nums)
    return expected_sum - actual_sum
