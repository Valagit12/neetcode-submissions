class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Expand nums to solve the question
        nums = [1] + nums + [1]

        # dp[(i, j)] will represent the best solution from nums[i: j + 1]
        dp = {}

        def dfs(i, j):
            # The left pointer i, and right pointer j will approach each other. If the left pointer ever passes the right pointer,
            # we have an empty subproblem, meaning nums = []
            if i > j:
                return 0
            # If have already solved, just return
            if (i, j) in dp:
                return dp[(i, j)]
            
            # Iterate through each element in the subproblem (from i to j)
            dp[(i, j)] = 0
            for n in range(i, j + 1):
                temp = nums[i - 1] * nums[n] * nums[j + 1]
                temp += dfs(i, n - 1) + dfs(n + 1, j)
                dp[(i, j)] = max(dp[(i, j)], temp)
            return dp[(i, j)]
        
        return dfs(1, len(nums) - 2)



        