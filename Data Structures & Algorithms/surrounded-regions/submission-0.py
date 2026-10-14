class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        '''

        for each cell on edges, if its an o
            do a dfs and add each o to seen

        for each o in the grid, if its not in seen, turn it to an x
        '''

        ROWS, COLS = len(board), len(board[0])
        seen = set()

        def dfs(i, j):
            if (i >= 0 and i < ROWS and j >= 0 and j < COLS and (i, j) not in seen and board[i][j] != 'X'):
                seen.add((i, j))
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)


        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROWS - 1][c] == 'O':
                dfs(ROWS - 1, c)

        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COLS - 1] == 'O':
                dfs(r, COLS - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in seen:
                    board[i][j] = 'X'
        

        

