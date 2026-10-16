class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        furthest = nums[0] if nums[0] < len(nums) - 1 else len(nums) - 1
        jumps = 1
        for i in range(1, len(nums) - 1):
            j = nums[i]

            if i + j >= len(nums) - 1 and furthest != len(nums) - 1:
                jumps+=1
                return jumps
            elif furthest <= i and i + j > furthest:
                jumps+=1
                furthest = i + j
                   
        return jumps
