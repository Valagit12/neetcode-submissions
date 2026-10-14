class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp = {}

        # def isPalindrome(st):
        #     low = 0
        #     high = len(st) -1
        #     while low < high:
        #         if st[low] != st[high]:
        #             return False
        #         low+=1
        #         high-=1
        #     return True


        # def helper(st):
        #     if st in dp:
        #         return dp[st]
            
        #     elif isPalindrome(st):
        #         dp[st] = st
        #         return dp[st]
            
        #     a = helper(st[1:])
        #     b = helper(st[:-1])

        #     dp[st] = a if len(a) > len(b) else b
        #     return dp[st]
        
        # return helper(s)

        curMax = ''
        curMaxIDX = -1

        for i in range(len(s)):
            #odd length:

            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(curMax):
                    curMax = s[l:r+1]
                    curMaxIDX = i
                l-=1
                r+=1
            
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > len(curMax):
                    curMax = s[l:r+1]
                    curMaxIDX = i
                l-=1
                r+=1
        
        return curMax



#         abbc
#     abb     bbc
# ab    bb       bb   bc
# a b  b. b     b  b. b. c