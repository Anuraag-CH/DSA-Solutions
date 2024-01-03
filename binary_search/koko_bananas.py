# https://leetcode.com/problems/koko-eating-bananas/


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find  max of piles
        max_piles = max(piles)

        # binary search between min and max and find min k for hours given
        l = 1
        r = max_piles
        res = max_piles

        # write a function which takes in a number and piles list and returns true or false
        def can_eat(mid):
            num_of_hours = 0

            for p in piles:

                if p % mid == 0:
                    num_of_hours += p // mid
                else:
                    num_of_hours += p // mid + 1

            return num_of_hours <= h

        while l <= r:
            mid = (l + r) // 2

            if can_eat(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

