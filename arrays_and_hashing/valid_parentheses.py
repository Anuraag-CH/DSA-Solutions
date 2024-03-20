# https://leetcode.com/problems/valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ")}]":
                if not stack:
                    return False
                if i == ")" and stack.pop() != "(":
                    return False
                if i == "}" and stack.pop() != "{":
                    return False
                if i == "]" and stack.pop() != "[":
                    return False

            else:
                stack.append(i)

        return True if not stack else False

# Time complexity: O(n)
# Space complexity: O(n)
