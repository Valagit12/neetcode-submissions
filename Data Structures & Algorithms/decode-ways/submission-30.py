class Solution:
    def numDecodings(self, s: str) -> int:
        
        '''
        (1126)
        1 126
           1 26
              2 6

        '''

        dp = [-1] * len(s)

        def dfs(l, r):

            if l > r:
                return 1

            if dp[l] >= 0:
                return dp[l]
            
            if s[l] == '0':
                return 0
            
            res = dfs(l+1, r)
            if r - l + 1 >= 2 and int(s[l:l+2]) <= 26:
                res += dfs(l+2, r)

            dp[l] = res
            return dp[l]
        

        return dfs(0, len(s) - 1)
            
            
            


