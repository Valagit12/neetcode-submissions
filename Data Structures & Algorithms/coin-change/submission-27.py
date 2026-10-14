class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        given an integer array of coins
        coin[i] -> what kind of coin the ith coin is. 5 cents, 1 cent, etcc
        want to make given amount
            
                                                1 5 10
                                            /.     |       \
                                            1      5        10
                                           /     
                                      1   5  10
        '''

        n = len(coins)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for amount_to_test in range(1, amount + 1):
            for coin in coins:
                if amount_to_test - coin >= 0:
                    dp[amount_to_test] = min(dp[amount_to_test], 1 + dp[amount_to_test - coin])
        
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]

        