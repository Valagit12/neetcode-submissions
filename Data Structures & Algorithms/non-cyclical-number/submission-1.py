class Solution:
    def isHappy(self, n: int) -> bool:
        
        def breakk(num):
            res = 0
            while num != 0:
                res += (num % 10)**2
                num = num // 10
            return res

        seen = set()
        while n != 1:
            seen.add(n)
            n = breakk(n)
            print(n)
            if n in seen:
                return False
        
        return True