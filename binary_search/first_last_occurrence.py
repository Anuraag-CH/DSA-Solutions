class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            return [0, 0] if target == nums[0] else [-1, -1]

        first_occurence = -1
        last_occurrence = -1

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                first_occurence = mid
                r = mid - 1

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                last_occurrence = mid
                l = mid + 1

            elif target > nums[mid]:
                l = mid + 1

            else:
                r = mid - 1

        return [first_occurence, last_occurrence]
