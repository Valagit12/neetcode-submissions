class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #     '''
    #     Given array of integers prices
    #     prices[i] = price of neetcoin on ith day
    #     after sell, cannot buy another one on the next day
    #     Only own one neetcoin at a time -> if have bought, must sell
    #     max profit
        

    #                                               /     1 3 4 0 4
    #                                         buy                                         wait
    #                                     /   -1   \                                        0
    #                                 sell            wait
    #                 ____________/    2           /   -1  \
    #             wait                           sell       wait
    #             2                                3           -1
    #         /       \___                       /        
    #     buy             wait                wait
    #       2              2                    3
    #   /     \          /    \             /       \
    #  sell    wait     buy.  wait        buy     wait
    #   6        2       -2    2            -1      3
    #     '''
        #dp[i][0] Max profit you can achieve from today on, if not holding any stock
        #dp[i][1] Max profit you can achieve from today on, if holding a stock   
        dp = [[0, 0] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            # Not holding any stocks today
            dp[i][0] = max(
                dp[i + 1][0], #dont buy anything today
                dp[i + 1][1] - prices[i] # since dp[i+1][1],[i+1][1] means you have a stock tommorrow
                )
            
            # Are holding stocks to sell
            dp[i][1] = max(
                dp[i+1][1], # dont sell today
                prices[i] + dp[i+2][0] # sell today, and find out what your profit is two days from now (cooldown)\
            )
        
        return dp[0][0]









