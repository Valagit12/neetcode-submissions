class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''

        1.   2     3.   4.   5

                      7      6
        '''
        slow = nums[0]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        print(slow, fast)
        
        left = 0
        while left != slow:
            slow = nums[slow]
            left = nums[left]
        
        return left
