# https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dp(nums,i,s1,s2,cache):
            
            if i >= len(nums):
                return s1 == s2
            
            if (i,s1,s2) in cache :
                return cache[(i,s1,s2)]
            
            
            cache[(i,s1,s2)] = dp(nums,i+1,s1+nums[i],s2,cache) or dp(nums,i+1,s1,s2+nums[i],cache)

            return cache[(i,s1,s2)]
        
        return dp(nums,0,0,0,{})

#Space complexity: O(n^2)
#Time complexity: O(n^2)
    

    
