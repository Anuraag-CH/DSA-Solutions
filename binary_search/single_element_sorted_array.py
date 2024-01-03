from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == nums[mid - 1]:
                if (mid - 1) % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (mid + 1) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                return nums[mid]
