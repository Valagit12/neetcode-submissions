class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        dp = [-1]*len(nums)

        def helper(i):
            if dp[i] != -1:
                return dp[i]

            if i == 0 or i == 1:
                dp[i] = nums[i]
                return dp[i]
            elif i == 2:
                dp[i] = nums[i] + helper(i-2)
                return dp[i]
            
            dp[i] = max(helper(i-2), helper(i-3)) + nums[i]
            return dp[i]

        a = helper(len(nums) - 1)
        b = helper(len(nums) - 2)
        s = max(a, b)
        return s