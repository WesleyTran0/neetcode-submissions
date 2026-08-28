class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        best = 0

        for i in prices:
            low = min(low, i)
            best = max(best, i - low)
        
        return best
