class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countBitsHelp(m):
            res = 0
            # print(m)
            while m > 0:
                if m % 2 == 1:
                    res+=1
                m = m // 2
            return res
        
        ans = []
        for i in range(n + 1):
            ans.append(countBitsHelp(i))

        
        return ans
