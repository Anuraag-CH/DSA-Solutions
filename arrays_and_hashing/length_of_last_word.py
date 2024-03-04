# https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.strip()
        return len(s.split()[-1]) 

# Time complexity: O(n)
# Space complexity: O(n)