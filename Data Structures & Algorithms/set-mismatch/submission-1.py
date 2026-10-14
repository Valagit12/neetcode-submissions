class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        seen = [0] * len(nums)

        for i in range(len(nums)):
            seen[nums[i] - 1] += 1
        
        print(seen)
        
        first = -1
        twice = -1
        for i in range(len(seen)):
            if seen[i] == 2:
                twice = i + 1
            if seen[i] == 0:
                first = i + 1
        
        return [twice, first]


         