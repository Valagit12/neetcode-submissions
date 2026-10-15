class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        currSum = 2/-1/4/2 = max(n, maxSum + n)
        maxSum = 2/4 = max(currSum, maxSum)

        2, -3, 4, -2, 2, 1, -1, 4
        '''
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0

        currSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            currSum = max(n, currSum + n)
            maxSum = max(currSum, maxSum)
        
        return maxSum

        