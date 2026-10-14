class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize the DP
        #dp[i][j] = the minnimum number of edits to make word1[i:] = word2[j:]
        # We have len(word1) + 1 rows because when i = len(word1), word1 is empty, which we have to account for,
        # We have len(word2) + 1 columns because when j = len(word2), word2 is empty, which we have to account for,
        #Even if we didnt have to account for empty words, we would still need the extra row and column for the base case
        dp = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # word1 = abcd
        # word2 = abbdc
        # dp  a   b   b   d   c   
        # a   inf inf inf inf inf inf
        # b   inf inf inf inf inf inf
        # c   inf inf inf inf inf inf
        # d   inf inf inf inf inf inf
        #     inf inf inf inf inf inf

        # Now we populate the base cases
        # First, when word1 is empty (bottom row)
        for j in range(len(word2)):
            dp[len(word1)][j] = len(word2) - j
        # Second, when word2 is empty(right most column)
        for i in range(len(word1)):
            dp[i][len(word2)] = len(word1) - i
        # When both are empty, there need not be any changes made
        dp[-1][-1] = 0

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j],
                        dp[i][j+1],
                        dp[i+1][j+1]
                    )
        
        return dp[0][0]



