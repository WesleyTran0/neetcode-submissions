class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxSell = 0
        l = 0

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxSell = max(prices[r] - prices[l], maxSell)
        
        return maxSell
