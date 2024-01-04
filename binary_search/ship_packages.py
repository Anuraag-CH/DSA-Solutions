# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = sum(weights)

        def can_ship(capacity):
            days_needed = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > capacity:
                    days_needed += 1
                    curr_weight = weight
                else:
                    curr_weight += weight
            return days_needed <= days

        while l <= r:  
            mid = (l+r)//2
            if can_ship(mid):
                r = mid - 1
                res = min(res,mid)
            else:
                l = mid + 1
        
        return res