# https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

# Time complexity: O(n)
# Space complexity: O(n)
