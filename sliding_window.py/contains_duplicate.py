class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        j = 0

        nums_set = set()

        for i in range(0, len(nums)):
            if not (i - j) <= k:
                nums_set.remove(nums[j])
                j += 1

            if nums[i] in nums_set:
                return True
            nums_set.add(nums[i])

        return False
