# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1:
            return 0

        suffix_max = [0] * len(prices)
        max_num = 0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > max_num:
                max_num = prices[i]
            else:
                suffix_max[i] = max_num

        max_profit = 0
        for i in range(len(prices)):
            profit = suffix_max[i] - prices[i]
            max_profit = max(profit, max_profit)

        return max_profit
