class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        l, r = 0, 1

        output = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                output = max(output, prices[r] - prices[l])
            else:
                l = r
            r+=1
        return output