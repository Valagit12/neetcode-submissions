class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxChain = 0
        for num in numset:
            length = 1
            chain = 1
            while num + length in numset:
                length+=1
                chain+=1
            maxChain = max(maxChain, chain)    
        
        return maxChain
                
                  
        


        

