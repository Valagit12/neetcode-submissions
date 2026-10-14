class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    #                                             12
    #                         11                      7                                 2
    #             10         6   1               6       2 
    #         9.  5. 0     5 1           
    #     8. 4.  4 0 
    #  7 3.  3
    # ... 

        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins


