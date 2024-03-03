# https://leetcode.com/problems/minimum-number-game
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            res.append(nums[i+1])
            res.append(nums[i])
            i+=2
        return res

# Time complexity: O(nlogn)
# Space complexity: O(n)