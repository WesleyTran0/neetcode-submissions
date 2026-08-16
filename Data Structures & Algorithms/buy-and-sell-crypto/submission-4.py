class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, profit = 0, 0

        for r in range(1, len(prices)):
            
            profit = max(prices[r] - prices[l], profit)

            if prices[r] < prices[l]:
                l = r
        
        return profit