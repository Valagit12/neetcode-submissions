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
            
        '''
        in python, ints are complex cpython objects without fixed length, negatives operate as 2s complements, but arent stored that way
        the sign of a python int is an object field
        so when you init res = 0, its a positive int, even though all the bits at the start are 1 (since python ints are variable length)
        thus imagine you have 0000...(2scomplement representation of the sum in 32 bits)
        if res < (1 << 31), that means res < 0000...1(30 bits of 0), basically, we are detecting if res is negative or not
        if result is negative, we return res - (1 << 32), which guarantees a negative python int.
        '''

        return res if res < (1 << 31) else res - (1 << 32)
            
            

        