class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        lowest = prices[0]
        for i in prices:
            best = max(i - lowest, best)
            lowest = min(lowest, i)
        
        return best