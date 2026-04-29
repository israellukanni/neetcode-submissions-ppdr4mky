class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        minP = prices[0]

        for p in prices:
            minP = min(minP,p)
            res = max(res, p - minP)
        return res
        