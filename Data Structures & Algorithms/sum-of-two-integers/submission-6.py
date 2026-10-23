class Solution:
    def getSum(self, a: int, b: int) -> int:
        '''
        10100
        11110
         0010
        00001

        '''
        res = 0
        carry = 0
        for i in range(32):
            rightmostABit = ((a >> i) & 1)
            rightmostBBit = ((b >> i) & 1)

            add = rightmostABit ^ rightmostBBit
            add ^= carry
            if (rightmostABit and rightmostBBit) or (rightmostABit and carry) or (rightmostBBit and carry):
                # add = 0, rightA and rightB = 1
                carry = 1
            else:
                carry = 0
            
            res ^= add << i
            
        
        return res if res < (1 << 31) else res - (1 << 32)
            
            

        