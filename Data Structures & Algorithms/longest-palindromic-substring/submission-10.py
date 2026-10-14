class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        res = ''

        dp = [[False] * n for _ in range(n)]

        for length in range(n): 
            for start in range(n - length):
                end = start + length
                if length > 3:
                    print(s[start: end+1], dp[start+1][end-1])
                if length <= 2 and s[start] == s[end]:
                    dp[start][end] = True

                    if len(res) < len(s[start:end+1]):
                        res = s[start:end+1]
                
                elif dp[start + 1][end - 1] and s[start] == s[end]:
                    dp[start][end] = True

                    if len(res) < len(s[start:end+1]):
                        res = s[start:end+1]
            
        return res




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


                
