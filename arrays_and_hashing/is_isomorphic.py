# https://leetcode.com/problems/isomorphic-strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hashset = {}

        for i in range(0, len(s)):
            if s[i] in s_hashset:
                if s_hashset[s[i]] != t[i]:
                    return False

            else:
                s_hashset[s[i]] = t[i]

        t_hashset = {}

        for i in range(0, len(t)):
            if t[i] in t_hashset:
                if t_hashset[t[i]] != s[i]:
                    return False

            else:
                t_hashset[t[i]] = s[i]

        return True


#Time complexity: O(n)
#Space complexity: O(n)

