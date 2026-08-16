class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        last = prices[0]
        prof = 0
        for i in prices:
            prof = max(prof, i - last)
            last = min(last, i)
        return prof
