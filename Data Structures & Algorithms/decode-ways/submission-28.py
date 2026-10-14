class Solution:
    def numDecodings(self, s: str) -> int:
        
        '''
                                11261
                (1 1261)                                         (11 261)
    (1 1 262)               (1 12 61)                    (11 2 61)           (11 26 1)
(1 1 2 62) (1 1 26 2).  (1 12 6 1)

        '''

        dp = {}

        def dfs(st):
            if not st:
                return 1

            if st in dp:
                return dp[st]

            if st[0] == '0':
                return 0
            
          
            
            single = dfs(st[1:])
            res = single
            if len(st) >= 2 and int(st[0:2]) <= 26:
                double = dfs(st[2:])
                res = single + double
            dp[st] = res
            return res



            
        return dfs(s)
            


