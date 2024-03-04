# https://leetcode.com/problems/concatenation-of-array

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

# Time complexity: O(n)
# Space complexity: O(n)
    