# https://leetcode.com/problems/left-and-right-sum-differences


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = [0]

        r_sum = nums[-1]
        for n in range(len(nums) - 2, -1, -1):
            right_sum.insert(0, r_sum)
            r_sum += nums[n]

        l_sum = 0
        res = []

        for n in range(0, len(nums)):
            val = abs(l_sum - right_sum[n])
            res.append(val)
            l_sum += nums[n]

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)
