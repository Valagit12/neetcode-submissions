class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            x = i
            numOnes = 0
            while x != 0:
                rightmost = x & 1
                numOnes += 1 if rightmost == 1 else 0
                x = x >> 1
            ans.append(numOnes)
        return ans

