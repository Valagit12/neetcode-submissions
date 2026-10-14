class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def helper(nom):
            if nom in dp:
                return dp[nom]

            if nom == 1:
                dp[1] = 1
                return dp[1]
            elif nom == 2:
                dp[2] = 2
                return dp[2]
            
            dp[nom] = helper(nom - 1) + helper(nom - 2)
            return dp[nom]


        return helper(n)
    
                