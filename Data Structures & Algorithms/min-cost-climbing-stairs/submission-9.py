class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        if n == 0:
            return 0
        
        if n == 1:
            return cost[0]
        
        '''
                    
                                    goal
                                6: 1
                            5: 1
                        4: 1
                    3: 2        min(cost[1] + currcost[1], cost[2] + currcost[2])
                2: 1    min(cost[0] + currcost, cost[1] + currcost) = 1 + 0 = 1
            1: 2
        0: 1

        min cost at goal = min(cost at 2 and cost at 1)
        min cost at 2 = min(cost at 1 and cost at 0)
        '''

        cost1 = cost[0]
        cost2 = cost[1]

        for i in range(2, n):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]


        return min(cost[n - 1], cost[n - 2])

