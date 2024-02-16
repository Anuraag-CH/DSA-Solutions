# https://leetcode.com/problems/maximum-number-of-pairs-in-array

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        pair_set = set()

        for n in nums :
            if n in pair_set :
                pair_set.remove(n)
                count+=1
            else :
                pair_set.add(n)
        
        return [count,len(pair_set)]

# Time complexity: O(n)
# Space complexity: O(n)