# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(1) == True:
            return 1

        if isBadVersion(n - 1) == False:
            return n

        l = 1
        r = n

        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m) == False:
                l = m + 1

            elif isBadVersion(m) == True and isBadVersion(m - 1) == True:
                r = m - 1

            else:
                return m
