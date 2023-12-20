#https://leetcode.com/problems/search-in-rotated-sorted-array
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # edge cases
        if n == 1:
            return 0 if nums[0] == target else -1
        if nums[0] < nums[-1]:
            return self.search_ele(nums, target, 0, n - 1)

        l = 0
        r = n - 1

        # find the pivot
        while l <= r:
            mid = (l + r) // 2
            # return the index if the target is found
            if nums[mid] == target:
                return mid
            next = (mid + 1 + n) % n
            prev = (mid - 1 + n) % n

            if nums[mid] < nums[next] and nums[mid] < nums[prev]:
                pivot = mid
                break

            elif nums[mid] < nums[r]:
                r = mid - 1

            else:
                l = mid + 1
        
        result_1=self.search_ele(nums, target, 0, pivot - 1)
        result_2=self.search_ele(nums, target, pivot, n - 1) 
        return max(result_1, result_2)
        
    # find the target   
    def search_ele(self,nums, target, l, r):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1