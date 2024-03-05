# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1 :
            return strs[0]
        
        length_base_string = len(strs[0])

        i = 0
        while i < length_base_string:
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1  
    
        return strs[0][:i]


# Time complexity: O(n * m)
# Space complexity: O(1)
        