# https://leetcode.com/problems/guess-number-higher-or-lower
class Solution:
    def guessNumber(self, n: int) -> int:

        l = 1
        r = n

        while True :
            m = (l + r)//2

            value = guess(m)

            if value == 0 :
                return m
            
            if value == -1 :
                r = m-1
            else :
                l = m+1