class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        memo = {}

        def dfs(i, s_idx):
            if (i, s_idx) in memo:
                return memo[i, s_idx
                ]
            if i == len(t) or s_idx == len(s):
                memo[(i, s_idx)] = s_idx == len(s)
                return s_idx == len(s)
            
            if s[s_idx] == t[i]:
                memo[(i, s_idx)] = dfs(i+1, s_idx + 1)
                return memo[(i, s_idx)] 

            memo[(i, s_idx)] = dfs(i + 1, s_idx)
            return memo[(i, s_idx)]
        
        return dfs(0, 0)