class Solution:
    def reverse(self, x: int) -> int:
        '''
        2^ 31
        
        1234

        1234 % 10 = 4
        1234 // 10 = 123
        res = 4

        123 % 10 = 3
        123 // 10 = 12
        res = res*10 + 3 = 40 + 3 = 43

        12 % 10 = 2
        12 // 10 = 1
        res = res*10 + 2 = 432
        '''

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res
