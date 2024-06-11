class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set() # Initialize list of seen elements.
        for i in nums: # Loop through elements in arr
            if i in seen: # If duplicate exists, return true
                return True
            seen.add(i) # Else, add element to list.
        return False # And return False (No duplicate)