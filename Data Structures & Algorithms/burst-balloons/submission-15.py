class Solution:

    def popBalloon(self, nums: List[int], coins: int, cache):
        
        key = tuple([coins, tuple(nums)])
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
            return (pow(nums[0], 3) * (len(nums) - 2)) + pow(nums[0], 2) + nums[0]

        else:
            calls = []

            for i in range(0, len(nums)):
                prev = 1 if i == 0 else nums[i - 1]
                post = 1 if i == len(nums) - 1 else nums[i + 1]
                added_coins = prev * nums[i] * post
                new_nums = nums.copy()
                new_nums.pop(i)
                calls.append(self.popBalloon(new_nums, coins + added_coins, cache))
            
            coins = max(calls)
            cache[key] = coins

        return cache[key]

    def maxCoins(self, nums: List[int]) -> int:
        cache = {}
        coins = 0
        result = self.popBalloon(nums, 0, cache)
        return result