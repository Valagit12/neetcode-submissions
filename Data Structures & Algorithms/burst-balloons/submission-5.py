class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        [1 4 2 -1 0 1]


        '''
        nums = [1] + nums + [1]

        dp = [[-1 for i in range(len(nums))] for _ in range(len(nums))]

        def dfs(l, r):
            if dp[l][r] >= 0:
                return dp[l][r]

            if l > r:
                return 0

            res = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(i+1, r) + dfs(l, i - 1)
                res = max(res, coins)
            
            dp[l][r] = res
            return res
        
        return dfs(1, len(nums) - 2)

            



        



            









