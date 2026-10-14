class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}

        def backtracking(idx):
            if idx in dp:
                return dp[idx]

            if idx == len(cost) - 1:
                dp[idx] = cost[idx]
                return cost[idx]
            elif idx == len(cost) - 2:
                dp[idx] = min(cost[idx] + cost[idx+1], cost[idx])
                return dp[idx]
            
            dp[idx] = cost[idx] + min(backtracking(idx + 1), backtracking(idx + 2))
            return dp[idx]


        
        return min(backtracking(0), backtracking(1))
