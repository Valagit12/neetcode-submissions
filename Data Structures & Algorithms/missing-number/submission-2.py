class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        3 0 1

        res = 3 + 0 - 3 = 0, 0 + 1 - 0 = 1, 1 + 2 - 1 = 2
        i = 2


        '''
        res = 0
        for num in nums:
            res ^= num
        
        for i in range(len(nums) + 1):
            res ^= i
        
        return res