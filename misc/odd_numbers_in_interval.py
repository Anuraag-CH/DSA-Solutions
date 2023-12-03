# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low == 0:
            low = 1
        
        total_numbers = high - low + 1

        if total_numbers % 2 == 0:
            return total_numbers // 2
        
        elif low % 2 == 0:
            return total_numbers // 2
        else:
            return total_numbers // 2 + 1
