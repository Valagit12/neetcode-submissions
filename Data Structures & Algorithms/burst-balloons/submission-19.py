class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(nums):
            key = tuple(nums)

            if key in cache:
                return cache[key]

            if len(nums) == 0:
                result = 0

            elif len(nums) == 1:
                result = nums[0]

            elif len(nums) == 2:
                product = nums[0] * nums[1]
                result = product + max(nums[0], nums[1])

            elif max(nums) == min(nums):
                result = (
                    nums[0] ** 3 * (len(nums) - 2)
                    + nums[0] ** 2
                    + nums[0]
                )

            else:
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