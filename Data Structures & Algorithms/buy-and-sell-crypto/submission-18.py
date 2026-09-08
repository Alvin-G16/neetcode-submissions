class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 1
        maxProfit = 0

        while s < len(prices):
            if prices[b] < prices[s]:
                currentProfit = prices[s] - prices[b]
                maxProfit = max(maxProfit, currentProfit)
            else:
                b = s
            s += 1
        return maxProfit