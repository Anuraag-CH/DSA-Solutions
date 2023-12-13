# https://leetcode.com/problems/minimum-size-subarray-sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1

        l = 0
        cur_sum = 0

        for r in range(0, len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                min_length = min(min_length, r - l + 1)

                cur_sum -= nums[l]
                l += 1

        return min_length if min_length < len(nums) + 1 else 0
