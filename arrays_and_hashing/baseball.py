# https://leetcode.com/problems/baseball-game


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == "C":
                stack.pop()

            elif i == "+":
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)

            elif i == "D":
                a = stack[-1]
                stack.append(2 * a)
            else:
                stack.append(int(i))

        return sum(stack)


# Time Complexity: O(n)
# Space Complexity: O(n)
