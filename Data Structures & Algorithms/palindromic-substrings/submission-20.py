class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[False] * n for _ in range(n)]

        for high in range(n):
            for low in range(high+1):
                    
                if s[low] == s[high] and (high - low <= 2 or dp[low + 1][high - 1]):
                    dp[low][high] = True
                    res += 1

        for i in range(n):
            for j in range(n):
                print(dp[i][j], end=' ')
            print()
        return res
    