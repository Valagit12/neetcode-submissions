class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [1 2 -3 4 0 5]

        # Method 1
        # [1 2 -3 1.5 4 5 2 0 5]
        #         
        #  min = -6
        #  max = -3
        #  product = 2
        # [1 2]
        

        # Method 2
        # [1 2 -3 4 0 5 2 3]
        #    l          r  
        #  prefix = 2
        #  suffix = 6 
        #  res = 6
        # nums = [1, 2, -3, 1.5, 4, 5, 2, 0, 100]
        cache = []
        res = []
        resmax = None
        curmin, curmax, = resmax, resmax
        n = len(nums)
        for i in range(n):

            l = nums[i]
            resmax = l if resmax == None else resmax
            curmax = 1 if curmax == None else curmax
            curmin = 1 if curmin == None else curmin
            print(l, curmax, curmin)
            temp = curmin
            if curmax * l < curmax:
                if l > curmax:
                    cache.append(l)
                else:
                    cache.append(resmax)
                    res.append(cache)
                    print(res)
                    cache = []
            else:
                cache.append(l)

            curmin = min(l, l*curmin, l*curmax)
            
            curmax = max(l, l*curmax, l*temp)

            resmax = max(curmax, resmax)
            if i == n -1:
                cache.append(resmax)
                res.append(cache)
        
        print(res)
        prod = 1
        for num in nums:
            prod *= num
        return res[-1][-1]




                 
