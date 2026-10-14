class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        isPalindrome = lambda string: string == string[::-1]

        def dfs(start, curr):
            if start == len(s):
                ans.append(curr)
                return
            
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    dfs(i + 1, curr + [s[start:i+1]])
        
        dfs(0, [])
        return ans

# a a b c d d c 
# aa ab bc cd dc
# aab abc bcd cdd ddc
# aabc abcd bcdd cddc
# aabcd abcdd bcddc
# aabcdd abcddc
# aabcddc
#                                          partition(aab)
#                                         choose between a and aa
#                         choose a                                                    choose aa
#                         partition(ab)                                           partition b
#                         choose between a                                            c

#                         choose a
#                         partition(b)
#                         choose between b

#                         choose b
#                         done.
                        
                        

# 'aabcddc'

