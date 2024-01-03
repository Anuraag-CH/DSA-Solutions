# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums) :

        nums1 = []
        nums2 = []
        res = []

        for i in nums:
            if i < 0:
                nums1.append(i**2)
            else:    
                nums2.append(i**2)
        
        nums1.reverse()
        
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            res.append(nums1[i])
            i += 1 
        
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res  
     
# Time Complexity: O(n)
# Space Complexity: O(n)