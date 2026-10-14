class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(nums, coins):
            key = (coins, tuple(nums))

            if key in cache:
                return cache[key]

            elif len(nums) == 0:
                cache[key] = coins

            elif len(nums) == 1:
                cache[key] = coins + nums[0]

            elif len(nums) == 2:
                product = nums[0] * nums[1]
                cache[key] = coins + max(product + nums[0], product + nums[1])

            elif max(nums) == min(nums):
                return (nums[0] ** 3 * (len(nums) - 2)) + nums[0] ** 2 + nums[0]

            else:
                calls = []

                for i in range(len(nums)):
                    prev = 1 if i == 0 else nums[i - 1]
                    post = 1 if i == len(nums) - 1 else nums[i + 1]

                    added_coins = prev * nums[i] * post

                    new_nums = nums.copy()
                    new_nums.pop(i)

                    calls.append(dfs(new_nums, coins + added_coins))

                cache[key] = max(calls)

            return cache[key]

        return dfs(nums, 0)