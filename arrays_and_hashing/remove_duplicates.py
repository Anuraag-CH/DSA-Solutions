# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1

        current_val = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != current_val:
                current_val = nums[i]
                nums[j] = current_val
                j += 1

        return j


# Time complexity: O(n)
# Space complexity: O(1)
