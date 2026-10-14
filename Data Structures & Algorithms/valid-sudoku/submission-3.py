class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        row major form: (i, j)
                index = i*len(row) + j
                0*3 + 0 = 0
                0*3 + 1 = 1
                0*3 + 2 = 2
                1*3 + 0 = 3
                1*3 + 1 = 4
                        ...
                index /3 = i.    
                0/3 = 0 
                1/3 = 0
                2/3 = 0
                3/3 = 1
                4/3 = 1
                ...

                index % 3= j
                0 % 0 = 0
                0 % 1 = 1
                ...
        '''

        for tile in range(9):
            validTiles = [0] * 9
            for i in range(3):
                for j in range(3):
                    row = (tile // 3)*3 + i
                    col = (tile % 3)*3 + j

                    print(i, j)

                    num = board[row][col]
                    if not board[row][col] == '.':
                        num = int(board[row][col])
                        validTiles[num-1]+=1
                        if validTiles[num - 1] > 1: return False
                    


        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])


        return True
        