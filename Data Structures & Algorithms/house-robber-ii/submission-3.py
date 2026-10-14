class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a = nums[1:]
        b = nums[:-1]
        print(b)

        return max(self.helper(a), self.helper(b))
    
        # [1 3 6 2 1]
        # [2, 5, 1, 2 ,8, 10, 2300, 12]
        # [12, 2, 5, 1, 2 ,8, 10, 1, 12, 2]
        # [2,9,8,3,6]
        # [6,2,9, 8, 3]
        # -1,0,1, 2, 3
        #    6 6 15 15 18     
        # 5 8 12 = 25
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        print(dp)
        return dp[-1]


        
