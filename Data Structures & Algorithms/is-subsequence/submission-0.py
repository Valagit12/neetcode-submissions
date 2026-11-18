class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        def dfs(i, s_idx, builtS):
            if i == len(t) or s_idx == len(s):
                return builtS == s
            
            if builtS == s:
                return True
            
            if s[s_idx] == t[i]:
                return dfs(i+1, s_idx + 1, builtS + t[i])
                
            return dfs(i+1, s_idx, builtS)
        
        return dfs(0, 0, '')