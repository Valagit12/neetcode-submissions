class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in s + 's']
        n = len(s)

        if n == 0:
            return 0

        '''
            312 01
             21

                3       31 X
            1       12
        2         0.    01X
      0.   01x    1     
    1
        '''
        
        dp[-1] = 1

        for i in range(n - 1, -1, -1):
            print(dp)
            char = s[i]
            
            if i < n - 1 and (char == '1' or (char == '2' and s[i+1] in '0123456')):
                dp[i] = dp[i+1] + dp[i+2]
            
            elif char == '0':
                dp[i] = 0

            else:
                dp[i] = dp[i+1]            

        return dp[0]


