class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        start = prices[0]

        for i in prices:
            start = min(start, i)
            best = max(best, i - start)
        
        return best