# https://leetcode.com/problems/maximum-number-of-balloons


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}

        for i in text:
            if i in "balon":
                d[i] = 1 + d.get(i, 0)

        if d == {}:
            return 0

        min_value = d.get("b", 0)

        for i in "balon":
            if i in "ol":
                min_value = min(min_value, d.get(i, 0) // 2)
            else:
                min_value = min(min_value, d.get(i, 0))

        return min_value

# Time complexity: O(n)
# Space complexity: O(1)