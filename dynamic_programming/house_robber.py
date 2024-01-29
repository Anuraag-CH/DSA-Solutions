# https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:

        def dfs(nums,i,cache):
            if i >= len(nums):
                return 0
            
            if i in cache :
                return cache[i]
            
            else :
                cache[i] = max(nums[i] + dfs(nums,i+2,cache), dfs(nums,i+1,cache))
            
            return cache[i]
        

        
        return dfs(nums,0,{})

#Space Complexity: O(n)
#Time Complexity: O(n)