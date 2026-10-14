class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        interleave s and t, where s has length n and t has length m means
        s1 + t1 + s2 + t2 ... 
        or starting with t
        basically, the interleaved substring must be a mix of the chaacters of both strings, in any way,
        as long as the elements of each string appear in order.

        To achieve this, |n - m| <= 1 meaning they strings s and t can at most be one longer than the other
        so take 'aaa' and 'bbb', or 'aa' and 'bbb'. Those both work, but 'a' and 'bbb' Does not

        to interleave 'aaa' and 'bbb',
        ababab or bababa
        to interleave 'aa' and 'bbb'
        abab

        aaa bbb
        aabbba

            a a a
        b
        b
        b       
                  T
        '''

        n, m = len(s1), len(s2)

        if len(s3) != n + m:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[-1][-1] = True

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                #choose from s2
                print(i, j)
                if i < m and s2[i] == s3[i + j] and dp[i+1][j] == True:
                    dp[i][j] = True
                #choose from s1
                if j < n and s1[j] == s3[i + j] and dp[i][j+1] == True:
                    dp[i][j] = True
        # print(dp)
        return dp[0][0]
    
                