class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        cache = {}

        def dfs(left, right):
            if right - left == 1:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            result = 0

            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]

                result = max(
                    result,
                    dfs(left, k) + coins + dfs(k, right)
                )

            cache[(left, right)] = result
            return result

        return dfs(0, n - 1)