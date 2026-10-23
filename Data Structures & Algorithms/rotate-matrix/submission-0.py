class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        7 4 1.  1
        0 0 0   1
        0 0 0.  1
        '''
        n = len(matrix)

        ans = [[0] * n for _ in range(n)]

        for i in range(n):
            b = n - i - 1
            for j in range(n):
                a = j
                ans[a][b] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = ans[i][j]
        

                