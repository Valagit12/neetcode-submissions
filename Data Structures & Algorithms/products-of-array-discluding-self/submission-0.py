class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        '''

        2 3 3 3 3 2





        '''

        lefts = [1] * len(nums)
        rights = [1] * len(nums)
        prod = 1
        for i, num in enumerate(nums):
            if i == 0:
                lefts[i] = 1
                prod = num
            else:
                lefts[i] = prod
                prod *= num
        
        prod = 1
        for j, num in enumerate(reversed(nums)):
            if j == 0:
                rights[len(nums) - 1 - j] = 1
                prod = num
            else:
                rights[len(nums) - 1 - j] = prod
                prod *= num
        
        ans = []
        for k in range(len(nums)):
            ans.append(lefts[k] * rights[k])
        
        return ans