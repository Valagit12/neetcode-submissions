class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        10111

        11101

        
        10000
        '''
        
        res = 0
        for i in range(32):
            rightmostbit = (n >> i) & 1
            res += rightmostbit << (31 - i)
        
        return res