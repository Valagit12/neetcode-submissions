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
        cache = [[-1] * n for _ in range(n)]

        def dfs(left, right):
            if right < left:
                return 0

            # Only one balloon remains in the interval.
            if right - left == 2:
                return nums[left] * nums[left + 1] * nums[right]

            if cache[left][right] != -1:
                return cache[left][right]

            result = 0
            boundaries = nums[left] * nums[right]

            for k in range(left + 1, right):
                coins = (
                    boundaries * nums[k]
                    + dfs(left, k)
                    + dfs(k, right)
                )

                if coins > result:
                    result = coins

            cache[left][right] = result
            return result

        return dfs(0, n - 1)