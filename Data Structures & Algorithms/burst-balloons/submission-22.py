class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [x for x in nums if x != 0]
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        # Preserve the original optimization.
        if min(nums) == max(nums):
            a = nums[0]
            return a**3 * (n - 2) + a**2 + a

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length

                for k in range(left + 1, right):
                    coins = (
                        nums[left] * nums[k] * nums[right]
                        + dp[left][k]
                        + dp[k][right]
                    )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]