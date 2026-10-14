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
        if len(nums) == 1:
            return nums[0]

        dp = [-1]*len(nums)

        for i, num, in enumerate(nums):
            if i <= 1:
                dp[i] = nums[i]
                continue
            elif i == 2:
                dp[i] = dp[0] + nums[2]
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        print(dp)
        return max(dp[-1], dp[-2])
             