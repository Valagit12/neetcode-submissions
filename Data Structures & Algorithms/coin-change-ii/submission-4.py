class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # '''

        #                          ________________________1 2 3__________
        #                         1                          2            3   
        #             ______/     |    \                  /    \          |
        #             1           2     3                1      2         1
        #           /   \         |     4                4      4         x     
        #         1       2       1                      x
        #                 4       4
        #         1               x
        #         4.  
                        
        #     Only generate a subtree if the currSum is less than result

        #     1 2 3

        #     Given [1], we can generate with 4 coins, 1 way
        #     Given [1, 2], we can generate with 4 coins or 3 coins or 2 coins, 3 ways
        #       0 1 2 3 4           
        #    x  0 0 0 0 0 
        #   i1  0 1 1 1 1
        #   i2  0 1 2 2 3
        #   i3  0 0 0 0 1
        #   dp[i][j] = how many ways can you make amount j + 1 with sublist 0 to i
        #             the number of ways you could make amount j+1 at i - 1, plus the amount of ways you could make j+1 - nums[i]
        #             dp[i-1][j] + dp[i][j - nums[i]]
        # '''
        n = len(coins)

        if amount == 0:
            return 1

        #amount + 1 x n + 1 matrix
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # print(dp)

        for i, coin in enumerate(coins):
            if coin >= 0 and coin <= amount:
                dp[i+1][coin] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - coins[i - 1] >= 0:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        # print(dp)
        return dp[-1][-1]

         