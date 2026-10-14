class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [-1] * len(cost)

        def helper(index):
            if index == 0:
                dp[0] = cost[0]
                return dp[0]
            elif index == 1:
                dp[1] = cost[1]
                return dp[1]
            
            dp[index] = min(helper(index - 1), helper(index - 2)) + cost[index]
            return dp[index]
        return min(helper(len(cost) - 1), helper(len(cost) - 2))


