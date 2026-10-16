class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        furthest = min(nums[0], len(nums) - 1)
        next_furthest = furthest
        jumps = 1

        # furthest is how far the current number of jumps can take me
        # next_furthest is how far you can go if you take one more jump.
        # This solution basically relies on the fact that you only take a jump, once i reaches furthest. That way, you know what the furthest index 
        # you can reach is. 

        # Try tracing the example below
        # [2, 3, 1, 1, 1, 1]


        for i in range(1, len(nums) - 1):
            j = nums[i]

            next_furthest = max(next_furthest, i + j)
            # Since you are guaranteed a solution, dont need to check for furthest >= len(nums) - 1
            if i == furthest and furthest < len(nums) - 1:
                jumps += 1
                furthest = next_furthest

        return jumps
