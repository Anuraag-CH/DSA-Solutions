# https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        #edge cases
        if len(nums) == 1:
            return 0
        #first and last elements
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        #loop through the array
        l = 1 
        r = len(nums)-2

        while  l <= r:
            
            mid = (l+r)//2

            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid

            if nums[mid]<nums[mid+1]:
                l = mid + 1 
            elif nums[mid]<nums[mid-1]:
                r = mid - 1
        
