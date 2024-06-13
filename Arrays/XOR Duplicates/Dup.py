# Given an array of elements, find the XOR of Numbers Which Appear Twice

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dup = set() # Initialize list of seen elements.
        xor_op = 0 # Initialize XOR operation
        for i in nums:
            if i in dup: # If duplicate exists, perform XOR operation
                xor_op^=i
            else:
                dup.add(i) # Else, add element to list and continue loop
        return xor_op

