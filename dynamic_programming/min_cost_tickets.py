from typing import List
# https://leetcode.com/problems/minimum-cost-for-tickets/


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i, current_day):
            if i >= len(days):
                return 0
            if (i,current_day) in dp:
                return dp[i,current_day]
            if days[i] < current_day:
                return dfs(i+1, current_day)
            else:
                dp[i,current_day] = min(dfs(i+1, days[i]+1)+costs[0], dfs(i+1, days[i]+7)+costs[1], dfs(i+1, days[i]+30)+costs[2])
                return dp[i,current_day]
        return dfs(0, days[0])
    

           