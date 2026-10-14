class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        1 2 3 4 8 12 9

        20
        3
        0

        '''


        for l in range(0, len(numbers)):
            for r in range(l+1, len(numbers)):
                leftnum = numbers[l]
                rightnum = numbers[r]

                print(l, r, leftnum, rightnum)
                if leftnum + rightnum == target:
                    return [l+1, r+1]
                
        return []

    
        