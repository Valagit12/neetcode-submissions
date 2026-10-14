class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # top down 
        # dp = [-1] * len(cost)

        # def helper(index):
        #     if index == 0:
        #         dp[0] = cost[0]
        #         return dp[0]
        #     elif index == 1:
        #         dp[1] = cost[1]
        #         return dp[1]
            
        #     dp[index] = min(helper(index - 1), helper(index - 2)) + cost[index]
        #     return dp[index]

        # return min(helper(len(cost) - 1), helper(len(cost) - 2))

        #bottom up
        # dp = [-1] * len(cost)

        # for i, n in enumerate(cost):
        #     if i == 0:
        #         dp[i] = cost[i]
        #     elif i == 1:
        #         dp[1] = cost[1]
        #     else:
        #         dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        # return min(dp[-1], dp[-2])

        #bottom up optimized for space
        one = cost[0]
        two = cost[1]

        for i, n in enumerate(cost):
            if i <= 1:
                continue
            
            temp = one
            one = two
            two = min(temp, two) + cost[i]
        
        return min(one, two)
