class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_idx = 0
        for t_idx in range(len(t)):
            if s_idx == len(s):
                return True
            if s[s_idx] == t[t_idx]:
                t_idx += 1
                s_idx += 1
            else:
                t_idx += 1
        
        return s_idx == len(s)

