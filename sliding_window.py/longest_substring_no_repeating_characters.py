# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_substring = 0
        distinct_elements = set()
        l = 0

        for r in range(0,len(s)):
            while s[r] in distinct_elements :
                distinct_elements.remove(s[l])
                l += 1
            
            distinct_elements.add(s[r])
            max_substring = max(max_substring,r-l+1)

        
        return max_substring
            




        

