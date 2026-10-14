class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        nums[1] = max(nums[0], nums[1])
        

        '''

        2 9 8    3      6
        2 9 10.  11     16 


        '''

        for i in range(2, n):
            print(i, nums[i], '|', nums[i-2] + nums[i], nums[i-1])
            nums[i] = max(nums[i - 2] + nums[i], nums[i - 1])
        
        return nums[-1]


        