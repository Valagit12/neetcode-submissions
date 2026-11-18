class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        def dfs(i, s_idx):
            if i == len(t) or s_idx == len(s):
                return s_idx == len(s)
            
            if s[s_idx] == t[i]:
                return dfs(i+1, s_idx + 1)
                
            return dfs(i+1, s_idx)
        
        return dfs(0, 0)