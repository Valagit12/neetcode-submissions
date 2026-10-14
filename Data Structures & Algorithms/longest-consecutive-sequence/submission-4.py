class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        2       
        20
        4
        10
        3
        4
        5
        '''

        res = 0
        store = set(nums)

        for num in nums:
            streak = 1
            curr = num

            while curr + 1 in nums:
                streak+=1
                curr+=1
            
            res = max(streak, res)
        
        return res