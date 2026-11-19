class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[] for _ in range(numRows)]
        print(dp)
        if numRows == 0:
            return 0
        dp[0] = [1]
        if numRows == 1:
            return [dp[0]]
        dp[1] = [1, 1]

        for i in range(2, numRows):
            print(dp)
            dp[i].append(1)
            for j in range(1, i):
                dp[i].append(dp[i - 1][j - 1] + dp[i-1][j])
            dp[i].append(1)
        return dp