# Return Indices of two numbers in an array that add up to a target element.
class Solution(object):
    def TwoSum(self, nums, target):
        for i in range (len(nums)): # Loop through num and compare
            for j in range (i+1, len(nums)): # Begin looping from the next num since its n>1
                if nums[j] + nums[i]== target: # or target - nums[i] (Less optmized tho)
                    return [i, j]
