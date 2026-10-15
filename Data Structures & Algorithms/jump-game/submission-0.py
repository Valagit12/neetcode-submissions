class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1 5 2 4 0 0 3 1
        # largest = 0/ 1/6
        # i = 0/1/2
        # num = 1/5/2
        # i == largest, so largest = max(0, 0 + 1)
        # i < largest so largest = max(1, 6)
        largest = 0
        for i in range(len(nums)):
            num = nums[i]

            if i > largest:
                return False
            
            largest = max(largest, i + num)
        
        return True
    



    
