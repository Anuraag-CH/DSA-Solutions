# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for i in range (0,len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]],i]
            
            d[nums[i]] = i
        

# Time complexity: O(n)
# Space complexity: O(n)
        
    

