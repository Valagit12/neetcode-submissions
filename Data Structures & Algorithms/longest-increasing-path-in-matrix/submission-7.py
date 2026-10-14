class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * n for _ in range(m)]

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]  # (dy, dx)
        def dfs(r: int, c: int) -> int:

            if dp[r][c] >= 0:
                return dp[r][c]
            best = 1
            for dy, dx in dirs:
                nr, nc = r + dy, c + dx
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            dp[r][c] = best
            return best

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans
            
        return ans

                
        