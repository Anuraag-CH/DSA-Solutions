# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l =0 
        r = len(letters) - 1

        ceil = None

        while l <= r :
            mid = (l + r) // 2

            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
                ceil = min(ceil, letters[mid]) if ceil else letters[mid]        
        return ceil if ceil else letters[0]
        