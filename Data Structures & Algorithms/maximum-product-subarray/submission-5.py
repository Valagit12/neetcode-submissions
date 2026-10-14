class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        [2, 4, -3, 5]

        [2 4 -3     5      8      -2     0   0   1   2   67       -8        ]
         
    max  2 8  8    40.    48                            
    min. 2 2 -24.  -120                           
    ans. 2 8  8    40                       
        
        for i in n: find coint negatives and track index

        if odd:
            loop through array while tracking product. 
            once reach negative, add product to a tracked max and reset
            so 
            i 0 -> 2, product = 8, [2]=-3, reset
            i 3 -> 5, product = 40, 
            treat 0s as if they were 1, track product, reset but also do the comparison thing. 
            1 * 2 * 67
        
        if evendo whole subarray
        '''
        if len(nums) == 0:
            return 0

        '''
        2 4 -3 5
        cmax 2 8 8. 40
        cmin 2 2 -3 -15
        tmax 2 8 8. 40

        -3 0 -2
        cmax 
        cmin
        tmax
        '''

        curmax = nums[0]
        curmin = nums[0]
        truemax = nums[0]
    
        if len(nums) == 1:
            return truemax

        for i, num in enumerate(nums[1:]):
            maxtemp = curmax
            curmax = max(curmax * num, curmin * num, num)
            curmin = min(maxtemp * num, curmin* num, num)

            truemax = max(maxtemp, curmax, truemax)
        
        return truemax
        
        
            
            
            
            