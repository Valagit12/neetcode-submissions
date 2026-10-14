class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Given array of integers nums and an integer target

        For each number in the array, choose to either add or subtract to total sum

        How many different ways sum to target

                                __________2 2 2_________                    target = 4
                        ________2_____             ____-2_______
                    ___4___        ___0___      __0___      ___-4____    
                    6.     2.     2.      -2.   2.    -2    -2       -6

                    0 1 2 3 4
                    1 0 1 0 0



                                __________2 4 2_________.           target = 6
                        ________2_____             ____-2_______
                    ___6___        ___-2___      __2___      ___-6____    
                    8.     4.     0.      -4.   0.    4    -4       -8

                    
                  {0 = 1 }


                  2 

                  


                
        '''

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp

        return dp[target]
            




