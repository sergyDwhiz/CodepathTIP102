# Contains Duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach 1: Use a set to track seen elements
        # Approach 2: Check if the length of the list is different from length
        #               of the set of the list.
        return len(set(nums)) != len(nums)

        # Approach 1:
        seen = set()
        for i in nums:
            for j in nums:
                return True # Number found in set
            seen.add(i)
        return False