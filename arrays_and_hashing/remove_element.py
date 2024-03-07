# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        j = 0

        for i in range(0,len(nums)):

            if nums[i] != val :
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
        
        return j
            

# Time complexity: O(n)
# Space complexity: O(1)        
            

            


