class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        currSum = 2/-1/4/2 = max(n, maxSum + n)
        maxSum = 2/4 = max(currSum, maxSum)

        2, -3, 4, -2, 2, 1, -1, 4
        '''
        maxsub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxsub = max(maxsub, curSum)
        return maxsub
        