# https://leetcode.com/problems/search-insert-position/

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        floor = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                l = mid + 1
                floor = max(floor, mid)

            else:
                r = mid - 1

        return floor + 1

