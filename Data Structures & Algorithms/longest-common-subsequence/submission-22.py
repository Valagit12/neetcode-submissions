class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        '''
        cat
         ^
        crabt
        ^ 
        '''



        m, n = len(text1), len(text2)
        dp = {}

        def dfs(p1, p2):
            key = (p1, p2)
            print(p1, p2)
            if key in dp:
                return dp[key]

            if p1 == m - 1 and p2 == n - 1:
                dp[key] = 1 if text1[p1] == text2[p2] else 0
                print('base')
                return dp[key]
           
            if text1[p1] == text2[p2]:
                dp[key] = dp.get(key, 0) + 1
                if p1 < m - 1 and p2 < n - 1:
                    dp[key] += dfs(p1 + 1, p2 + 1)
                return dp[key]
                
                    

            firstup, secondup = 0, 0
            if p1 < m - 1:
                firstup = dfs(p1 +1, p2)
            if p2 < n - 1:
                secondup = dfs(p1, p2 + 1)
            print('triple')
            dp[key] =  max(firstup, secondup)
            return dp[key]
        
        return dfs(0, 0)
            

            

