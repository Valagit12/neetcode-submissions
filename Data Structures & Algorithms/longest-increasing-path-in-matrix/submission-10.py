class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1] * m for _ in range(n)]

        nex = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i, j):
            if dp[i][j] >= 0:
                return dp[i][j]
            
            res = 1
            for y, x in nex:
                nexty, nextx = i + y, j + x
                if 0<= nextx < m and 0 <= nexty < n and matrix[nexty][nextx] > matrix[i][j]:
                    res = max(res, 1 + dfs(nexty, nextx))
            
            dp[i][j] = res
            return res
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans

                
        