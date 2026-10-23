class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        10111

        23/ 2 = 11.5
        11 / 2 = 5.5
        5 / 2 = 2.5
        2 / 2 = 1
        1/ 2 = 0.5
        '''

        res = 0
        while n > 0:
            n &= n - 1
            res += 1
        
        return res
            