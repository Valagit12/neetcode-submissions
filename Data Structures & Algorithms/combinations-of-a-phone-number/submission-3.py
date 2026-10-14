class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        A = ord('a')


        '''
        0, 1, 2 <- 1 (x - 1)*3 +1. +2.  
        3, 4, 5 <- 2  (2 - 1)*3 = 3 + 1 = 4, +2 = 5
        6, 7, 8 <- 3 
        9, 10, 11 <- 4
        ...
        '''

        ans = []

        if not digits:
            return ans
        def dfs(i, curr):
            if i == len(digits):
                ans.append(curr)
                return
            if digits[i] == '7':
                dfs(i + 1, curr + 'p')
                dfs(i + 1, curr + 'q')
                dfs(i + 1, curr + 'r')
                dfs(i + 1, curr + 's')
            elif digits[i] == '8':
                dfs(i + 1, curr + 't')
                dfs(i + 1, curr + 'u')
                dfs(i + 1, curr + 'v')
            elif digits[i] == '9':
                dfs(i + 1, curr + 'w')
                dfs(i + 1, curr + 'x')
                dfs(i + 1, curr + 'y')
                dfs(i + 1, curr + 'z')
            else:
                dfs(i + 1, curr + chr(A + (int(digits[i]) - 2)*3))
                dfs(i + 1, curr + chr(A + (int(digits[i]) - 2)*3 + 1))
                dfs(i + 1, curr + chr(A + (int(digits[i]) - 2)*3 + 2))

        dfs(0, '')
        return ans
        