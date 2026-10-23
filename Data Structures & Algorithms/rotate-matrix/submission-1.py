class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        7 4 1.  1
        0 0 0   1
        0 0 0.  1
        '''
        n = len(matrix)

        ans = [[0] * n for _ in range(n)]

        # Transpose
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i] = matrix[i][::-1]
        


        

                