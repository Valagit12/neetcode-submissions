class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        #empty?
        # [4 2 7]
        
        # 1 4 2                       4 2 7            2 7 1
        # 1 2 7| 2 7 1         1 4 7| 4 7 1        1 4 2 | 4 2 1
        # 1 7 1| 1 2 1         1 7 1| 1 4 1        1 2 1 | 1 4 1
        # 29      16             91.   88           24      26
        dp = {}

        def dfs(l, r):

            if l > r:
                return 0

            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r) ] = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            
            return dp[(l, r)]

        
        return dfs(1, len(nums) - 2)

        



            









