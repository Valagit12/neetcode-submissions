class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        maxP = 0
        minBuy = prices[0]

        for num in prices:
            maxP = max(maxP, num - minBuy)
            minBuy = min(num, minBuy)
        
        return maxP
        