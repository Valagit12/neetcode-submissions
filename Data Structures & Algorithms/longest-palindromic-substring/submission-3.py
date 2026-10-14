class Solution:
    def isPalindrome(self, s):
        l=0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            for j in range(i, n):
                stest = s[i:j+1]
                if self.isPalindrome(stest) and len(stest) > len(res):
                    res = stest
        return res

                
