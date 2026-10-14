class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        # dp = [-1]*len(nums)

        # def helper(i):
        #     if i < 0:
        #         return 0

        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = max(helper(i-2), helper(i-3)) + nums[i]
        #     return dp[i]

        # a = helper(len(nums) - 1)
        # b = helper(len(nums) - 2)
        # s = max(a, b)
        # return s

        #bottom up
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]
             