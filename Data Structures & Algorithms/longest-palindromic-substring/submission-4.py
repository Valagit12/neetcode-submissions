class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(st):
            l = 0
            r = len(st) - 1

            while l <= r:
                if st[l] != st[r]:
                    return False 
                l+=1
                r -= 1
            return True


        n = len(s)
        
        res = ''

        for length in range(0, n): 
            for start in range(n):
                end = start + length
                temps = s[start:end+1]
                if isPalindrome(temps) and len(temps) > len(res):
                    res = temps
        
        return res


                
                



        return ''



        #a 0 0 
        #b 1 1
        #a 2 2
        #b 3 3
        #d 4 4
        #ab 0 1
        #ba 1 2
        #ab 2 3
        #bd 3 4
        #aba 0 2
        #bab 1 3
        #abd 2 4
        #abab 0 3
        #babd 1 4
        #ababd 0 4


                
