class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        cat = i
         ^     
        crabt = j 
          ^ 
        
            i = 1, j = 3
        cat[1:] == crabt[3:]
            at == bt
            (2,3) or (1, 4)
            (2,3) -> cat[2:] == crabt[3:]
                        t == bt
            (1, 5) -> cat[1:] == crabt[4:]
                        at == t

        dp 
        3   1   1   1   1   0
        2   2   2   1   1   0
        1   1   1   1   1   0
        0   0   0   0   0   0
        '''
        
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                char1, char2 = text1[i], text2[j]

                if char1 == char2:
                    dp[i][j] = 1 + dp[i+1][j+1]
                
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])


        return dp[0][0]
        

        


        
