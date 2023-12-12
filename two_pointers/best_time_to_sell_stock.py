class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        left = 0
        right = 1
        while left <= right and right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                max_profit = max(max_profit, prices[right]-prices[left])
                right += 1
        return max_profit
        