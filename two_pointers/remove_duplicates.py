# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        element = nums[0]
        element_repeated = 1 
        l = 1

        for r in range(1,len(nums)):
            if nums[r] == element :
                element_repeated += 1

                if element_repeated <=2 :
                    nums[l] = nums[r]
                    l +=1
    
            else :
                nums[l] = nums[r]
                element = nums[r]
                element_repeated = 1
                l += 1
        
        return l