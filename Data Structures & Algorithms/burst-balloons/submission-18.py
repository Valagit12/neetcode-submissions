class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(nums):
            if not nums:
                return 0

            key = tuple(nums)

            if key in cache:
                return cache[key]

            result = 0

            for i in range(len(nums)):
                prev = 1 if i == 0 else nums[i - 1]
                post = 1 if i == len(nums) - 1 else nums[i + 1]

                added_coins = prev * nums[i] * post

                new_nums = nums.copy()
                new_nums.pop(i)

                result = max(result, added_coins + dfs(new_nums))

            cache[key] = result
            return result

        return dfs(nums)