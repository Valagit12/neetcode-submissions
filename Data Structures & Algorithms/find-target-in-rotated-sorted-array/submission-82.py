class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        1 2 3 4 5 6
        
        2 3 4 5 6 1
        3 4 5 6 1 2
        

        6 1 2 3 4 5
        5 6 1 2 3 4

        4 5 6 1 2 3 
        '''      
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            lvalue, rvalue, midvalue = nums[l], nums[r], nums[mid]

            if target == midvalue:
                return mid

            if midvalue >= lvalue:
                if target <= midvalue and target >= lvalue:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= midvalue and target <= rvalue:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1         
            
            
        