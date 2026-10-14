class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(posx, posy):
            if posy == m - 1 and posx == n - 1:
                return 1
            
            res = 0
            
            if posy < m:
                res += dfs(posx, posy+1)
            
            if posx < n:
                res += dfs(posx + 1, posy)
            
            return res
        
        return dfs(0,0)
                
            
