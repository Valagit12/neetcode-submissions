class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 6, 1, 5, 4

        # 6 1
        # 6 5 
        # 6 4
        # 6 1 5
        # 6 5 4
        # 6 1 5 4 


        dp = [-1] * len(nums)

        def dfs(curr):
            if curr >= len(nums):
                return 1

            if dp[curr] >= 0:
                return dp[curr]
                            
            res = 1
            for i in range(curr +1 , len(nums)):
                if nums[i] > nums[curr]:
                    res = max(res, dfs(i) + 1)


            dp[curr] = res
            return res
        
        return max([dfs(i) for i in range(len(nums))])


            






        