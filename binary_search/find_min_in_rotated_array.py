# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            next = (mid + 1 + n) % n
            prev = (mid - 1 + n) % n

            if nums[mid] < nums[next] and nums[mid] < nums[prev]:
                return nums[mid]

            elif nums[mid] < nums[r]:
                r = mid - 1

            else:
                l = mid + 1

