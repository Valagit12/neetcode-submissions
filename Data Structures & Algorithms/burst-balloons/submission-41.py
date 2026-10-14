class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Fast path for identical balloons.
        if min(nums) == max(nums):
            a = nums[0]
            return a**3 * (n - 2) + a**2 + a

        nums = [1] + nums + [1]
        n = len(nums)
        # A 2D array where cache[i][j] represents the best answer for nums[i: j + 1].
        cache = {}

        def dfs(left, right):
            if right < left: # if right < left, then we have an empty subproblem, meaning the subproblem is checking an empty nums list, its a base case
                return 0
            if (left, right) in cache: # if the solution exists in the cache, return it
                return cache[(left,right)]
            
            cache[(left, right)] = 0
            for k in range(left, right + 1):
                # for each num[k], we consider it to be the last balloon we pop
                # So as the last balloon we pop, it will be multiplied by the boundaries at right + 1 and left - 1
                coins = nums[k] * nums[left - 1] * nums[right + 1]
                # We also want to get the estimate of what it will be after the left and right subproblems are considered for each coin
                coins += dfs(left, k - 1) + dfs(k + 1, right)
                # Choose the largest one as the answer
                cache[(left,right)] = max(cache[(left,right)], coins)

            return cache[(left,right)]

        return dfs(1, n - 2)