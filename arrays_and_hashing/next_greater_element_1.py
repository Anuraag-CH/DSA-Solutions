# https://leetcode.com/problems/next-greater-element-i


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # initialize dict to store result of next greater elements of nums2
        dict = {}

        # To keep track of the next greater elements
        stack = []

        # loop over values of nums2 to get the next greater element and store in the dict
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                dict[nums2[i]] = stack[-1]
            else:
                dict[nums2[i]] = -1

            stack.append(nums2[i])

        # get the values for elements in nums1 and return the result
        for i in range(0, len(nums1)):
            nums1[i] = dict[nums1[i]]

        return nums1
