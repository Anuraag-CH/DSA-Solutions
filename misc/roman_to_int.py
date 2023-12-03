# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_literals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        for i in range(len(s)):
            if s[i] == "I" and i + 1 < len(s) and s[i + 1] in "VX":
                ans = ans - 1
            elif s[i] == "X" and i + 1 < len(s) and s[i + 1] in "LC":
                ans = ans - 10
            elif s[i] == "C" and i + 1 < len(s) and s[i + 1] in "DM":
                ans = ans - 100
            else:
                ans = ans + roman_literals[s[i]]

        return ans
