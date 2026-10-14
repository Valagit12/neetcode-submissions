class Solution:
    def rob(self, nums: List[int]) -> int:
        
    #    2 9 8 3 6 5 4 1 3
        if len(nums) == 1:
            return nums[0]
        elif len(nums) < 0:
            return 0

        dp1 = {}
        dp2 = {}

        def dfs(idx, n, dp):
            if idx in dp:
                return dp[idx]

            if idx == n - 1:
                print('here')
                dp[idx] = nums[idx]
                print(idx, dp, dp[idx])
                return nums[idx]
            elif idx == n - 2:
                print('here2')
                dp[idx] = max(nums[idx], nums[idx+1])
                print(idx, dp, dp[idx])
                return dp[idx]
            print('here3')
            dp[idx] = max(nums[idx] + dfs(idx + 2, n, dp), dfs(idx+1, n, dp))
            print(idx, dp, dp[idx])
            return dp[idx]
            
        return max(dfs(0, len(nums) - 1, dp1), dfs(1, len(nums), dp2))





       
      


        
