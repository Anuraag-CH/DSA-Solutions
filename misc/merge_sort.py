class Solution:
    def sortArray(self, nums):
        if len(nums) > 1:
            middle = len(nums) // 2

        else:
            return nums

        arr1 = nums[0:middle]
        arr2 = nums[middle : len(nums)]

        # call sortArray on two arrays
        arr1 = self.sortArray(arr1)
        arr2 = self.sortArray(arr2)

        # merge
        c = self.merge(arr1, arr2)

        return c

    def merge(self, arr1, arr2):
        res = []
        l = 0
        r = 0

        while l < len(arr1) and r < len(arr2):
            if arr1[l] < arr2[r]:
                res.append(arr1[l])
                l += 1
            else:
                res.append(arr2[r])
                r += 1

        if l == len(arr1):
            res.extend(arr2[r:])
        else:
            res.extend(arr1[l:])

        return res
