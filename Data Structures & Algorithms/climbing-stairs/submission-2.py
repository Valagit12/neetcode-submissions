class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n

        def helper(nom):
            if nom in dp:
                return dp[nom]

            if nom == 0:
                dp[0] = 1
                return dp[0]
            elif nom == 1:
                dp[1] = 2
                return dp[1]
            
            dp[nom] = helper(nom - 1) + helper(nom - 2)
            return dp[nom]


        return helper(n-1)
    
                