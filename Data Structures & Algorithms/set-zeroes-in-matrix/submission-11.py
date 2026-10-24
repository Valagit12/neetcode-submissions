class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''

        103128910
        405908883
        608737099
        128012120
        283812161
        '''

        COLS, ROWS = len(matrix[0]), len(matrix)
        rowZero = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowZero = True
        
        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(ROWS):
                matrix[i][0] = 0

        if rowZero:
            for i in range(COLS):
                matrix[0][i] = 0
        
        
                

        
        