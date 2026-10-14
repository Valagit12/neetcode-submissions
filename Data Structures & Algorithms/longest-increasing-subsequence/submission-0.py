class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, curr):
            if curr >= len(nums):
                return 0
            
            res = dfs(prev, curr+1)

            if prev == -1 or nums[prev] < nums[curr]:
                res = max(res, dfs(curr, curr+1) + 1)
            print(prev, curr, res)
            return res
        
        return dfs(-1, 0)









        