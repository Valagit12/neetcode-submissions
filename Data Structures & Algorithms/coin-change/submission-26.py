class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * amount + [-1]

        def helper(t):
            if t == 0:
                dp[0] = 0
                return 0
            if dp[t] >= 0 or dp[t] == -5:
                return dp[t]
            
            
            curmin = None
            for coin in coins:
                if t - coin >= 0:
                    temp = helper(t-coin)
                    curmin = temp if (curmin == None or (temp < curmin)) and temp >= 0 else curmin
            if curmin == None:
                dp[t] = -5
                return dp[t]
            dp[t] = curmin+1
            return dp[t]
        ans = helper(amount)
        return ans if ans >= 0 else -1

        
        


