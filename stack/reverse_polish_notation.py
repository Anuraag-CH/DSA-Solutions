# https://leetcode.com/problems/evaluate-reverse-polish-notation


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                nums1 = stack.pop()
                nums2 = stack.pop()

                if token == "+":
                    val = (nums2) + (nums1)

                elif token == "-":
                    val = (nums2) - (nums1)

                elif token == "*":
                    val = (nums2) * (nums1)

                else:
                    val = abs(nums2) // abs(nums1)
                    if nums1 < 0 and nums2 < 0:
                        val *= 1
                    elif nums1 < 0 or nums2 < 0:
                        val *= -1

                stack.append(val)

            else:
                stack.append(int(token))

        return stack[-1]
