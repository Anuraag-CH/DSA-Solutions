# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize variables
        max_sum = 0
        cur_sum = 0
        set_distinct = set()
        l = 0

        # Loop over nums
        for r in range(len(nums)):
            # Remove elements from the left until the set is distinct
            while nums[r] in set_distinct:
                cur_sum -= nums[l]
                set_distinct.remove(nums[l])
                l += 1
            
            # Add the current element to the window
            cur_sum += nums[r]
            set_distinct.add(nums[r])

            # If the window size equals k, update max_sum and slide the window
            if (r - l + 1) == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[l]
                set_distinct.remove(nums[l])
                l += 1

        return max_sum
