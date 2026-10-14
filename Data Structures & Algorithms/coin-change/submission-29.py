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
            
        3 5    
        amount = 4

        for each amount from 0 to 4
            for each possible coin,
                check amount - coin >= 0
                    amount - coin = what needs to be added to this
                    take dp[amount - coin] + 1
                    do min(dp[amount], dp[amount-coin] + 1)
                
                
                    
                    

                


        no coins work.   1 works     1 works     1 works.  1 works     1 works, 5 works.   1,5                 
        0               0 + 1       1 + 1       2 + 1       3 + 1      1 -> dp[4] + 1       6c
        0                   1           2            3          4      5 -> 1 coin         
                                                                            5               6                7                9            10  11 12

        '''



        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        if not len(coins):
            return 0

        for i in range(1, amount+1):
            for coin in coins:
                if amount - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
                



