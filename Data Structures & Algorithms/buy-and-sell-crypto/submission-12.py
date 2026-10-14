class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) <= 1:
            return profit

        # [10, 9, 2 , 6 , 1, 1, 2 ,9 , 20, -1, 40]
        profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] >= prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
            
        return profit

            
            




            
            

        
        