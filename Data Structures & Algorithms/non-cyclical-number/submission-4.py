class Solution:
    def isHappy(self, n: int) -> bool:
        
        def breakk(num):
            res = 0
            while num != 0:
                res += (num % 10)**2
                num = num // 10
            return res

        slow = n
        fast = breakk(n)

        while fast != 1 and slow != fast:
            slow = breakk(slow)
            fast = breakk(breakk(fast))
        
        return fast == 1