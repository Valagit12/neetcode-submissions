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

        n = len(nums)
        dp = defaultdict(int)

        #dp[i] number of ways you can generate target sum.
        dp[0] = 1

        total = sum(nums)

        if abs(target) > total:
            return 0
        
        if (total + target) % 2 != 0:
            return 0

        total = 0

        for num in nums:
            next_dp = defaultdict(int)
            total+= num
            for j in range(0, total + 1):
                next_dp[j] += dp[j - num]
                next_dp[j] += dp[j + num]
                if j!= 0:
                    next_dp[-1 * j] += dp[(-1*j) - num]
                    next_dp[-1 * j] += dp[(-1*j) + num]
            dp = next_dp

        return dp[target]
            




