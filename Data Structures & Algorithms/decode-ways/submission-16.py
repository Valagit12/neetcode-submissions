class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]



"""        
'2101322'
 gfedcba   
6. a = 1
5. b = 2 
4. c = 2 
3. d = 2+2 = 4
2. e = 0 + 4 = 4
1. f = 1 + 4 = 5
0. g = 9
"""