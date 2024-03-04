# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1] 
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            next_max = max(max_val, arr[i])
            arr[i] = max_val
            max_val = next_max
        
    

# Time complexity: O(n)
# Space complexity: O(1)

