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
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            lvalue, rvalue, midvalue = nums[l], nums[r], nums[mid]

            if target == midvalue:
                return mid

            if lvalue <= midvalue:
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
            
            
        