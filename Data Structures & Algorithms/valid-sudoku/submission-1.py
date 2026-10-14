class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # condition 1

        for i in range(len(board)):
            digs = {i: 0 for i in range(1, 10)}
            for j in range(len(board[0])):
                num = board[i][j]
                
                if num =='.':
                    continue
                else:
                    num = int(num)

                if digs[num] == 0:
                    digs[num] += 1
                
                else:
                    return False
        

        for i in range(len(board)):
            digs = {i: 0 for i in range(1, 10)} 
            for j in range(len(board[0])):

                num = board[j][i]

                if num =='.':
                    continue
                else:
                    num = int(num)

                if digs[num] == 0:
                    digs[num] += 1
                
                else:
                    return False
        
        
        for subboard in range(9):
            digs = {i: 0 for i in range(1, 10)}
            '''
            0 3 6 -> 0
            1 4 7 -> 3
            2 5 8 -> 6

            0 1 2 -> 0
            3 4 5 -> 3
            6 7 8 -> 6

            '''
            min_col = (subboard%3) * 3
            min_row = (subboard//3) * 3

            for i in range(min_row, min_row + 3):
                for j in range(min_col, min_col + 3):
                    num = board[j][i]

                    if num =='.':
                        continue
                    else:
                        num = int(num)

                    if digs[num] == 0:
                        digs[num] += 1
                    
                    else:
                        return False
        
        return True




