class Solution:
    def climbStairs(self, n: int) -> int:
        
        # top down dp
        # dp = [-1] * n

        # def helper(nom):
        #     if nom in dp:
        #         return dp[nom]

        #     if nom == 0:
        #         dp[0] = 1
        #         return dp[0]
        #     elif nom == 1:
        #         dp[1] = 2
        #         return dp[1]
            
        #     dp[nom] = helper(nom - 1) + helper(nom - 2)
        #     return dp[nom]


        # return helper(n-1)


    
        # bottom up dp
        # dp = [1, 2]
        # for i in range(2, n):
        #     dp.append(dp[i-1] + dp[i-2])

        # return dp[n-1] 

        #memory optimization for bottom up dp
        one = 1
        two = 1
        for i in range(n - 1):
            temp = one
            one = two + one
            two = temp
        return one

