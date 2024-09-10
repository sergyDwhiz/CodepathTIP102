# Given two arrays, find number of Good pairs

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        count = 0
        for i in range (n):
            for j in range (m):
                if (nums1[i] % (nums2[j]*k)) ==0:
                    count += 1
        return count

