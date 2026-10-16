class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        furthest = min(nums[0], len(nums) - 1)
        next_furthest = furthest
        jumps = 1

        for i in range(1, len(nums) - 1):
            j = nums[i]

            next_furthest = max(next_furthest, i + j)

            if i == furthest and furthest < len(nums) - 1:
                jumps += 1
                furthest = next_furthest

        return jumps
