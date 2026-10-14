class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [1 2 -3 4 0 5]

        # Method 1
        # [1 2 -3 4 0 5]
        #         ^          
        #  product = 1 * 2 = 2 * -3 = -6 * 4 = -12 * 0 = 0
        #  min = 1 / 2 / -6 / -12 / -12 / 5
        #  max = 1 / 2 / 2 / 4.   /  4 
        

        # Method 2
        # [1 2 -3 4 0 5 2 3]
        #    l          r  
        #  prefix = 2
        #  suffix = 6 
        #  res = 6

        res = []
        resmax = nums[0]
        curmin, curmax, = resmax, resmax
        n = len(nums)
        for i in range(1, n):
            l = nums[i]


            temp = curmin
            curmin = min(l, l*curmin, l*curmax)
            curmax = max(l, l*curmax, l*temp)

            resmax = max(curmax, resmax)
        
        return resmax




                 
