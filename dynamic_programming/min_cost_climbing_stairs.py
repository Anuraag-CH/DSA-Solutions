# https://leetcode.com/problems/min-cost-climbing-stairs


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(cost, i, cache):
            if i >= len(cost):
                return 0
            if i == len(cost) - 1:
                return cost[i]

            if i in cache:
                return cache[i]

            else:
                cache[i] = cost[i] + min(
                    minCost(cost, i + 1, cache), minCost(cost, i + 2, cache)
                )
                return cache[i]

        cache = {}

        return min(minCost(cost, 0, cache), minCost(cost, 1, cache))


#Space Complexity: O(n)
#Time Complexity: O(n)

#alternate solution