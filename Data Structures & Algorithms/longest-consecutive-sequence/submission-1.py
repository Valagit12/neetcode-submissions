class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        found = set()
        
        if len(nums) == 0:
            return 0

        #O(n)
        minn = None
        maxx = None
        for num in nums:
            if minn == None or num < minn:
                minn = num

            if maxx == None or num > maxx:
                maxx = num
             
            found.add(num)
        
        chain = 1
        maxchain = 0
        for i in range(minn+1, maxx+1):
            if i in found:
                chain+=1
            else:
                maxchain = max(maxchain, chain)
                chain = 0
        maxchain = max(maxchain, chain)
        
        
        return maxchain

        


        

