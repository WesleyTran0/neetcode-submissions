class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best = 0
        bestL = prices[0]

        for i in range(len(prices)):
            bestL = min(bestL, prices[i])
            best = max(best, prices[i] - bestL)
        
        return best
