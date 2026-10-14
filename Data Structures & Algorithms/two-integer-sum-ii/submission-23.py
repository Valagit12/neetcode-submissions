class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        1 2 3 4 8 12 9
        l  
                 r                    

        10
        20
        3
        0

        '''

        l = 0
        r = len(numbers) - 1

        while l < r:

            leftnum = numbers[l]
            rightnum = numbers[r]
            summ = leftnum + rightnum
            if summ == target:
                return [l+1, r+1]
            elif summ < target:
                l+=1
            else:
                r-=1
        
            
        return []
                

    
        