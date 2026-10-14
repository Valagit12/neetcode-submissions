class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''

        currnode C -> A -> T
        '''
        POTENTIAL_NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        WIDTH = len(board[0])
        HEIGHT = len(board)

        def dfs(y, x, wordidx = 0, seen = set()):
            if wordidx == len(word) - 1:
                return word[wordidx] == board[y][x] and (x, y) not in seen
        
            if board[y][x] == word[wordidx] and (x, y) not in seen:
                seen.add((x,y))
                for dx, dy in POTENTIAL_NEIGHBOURS:
                    new_x, new_y = x + dx, y + dy
                    if new_x >= 0 and new_x < WIDTH and new_y >= 0 and new_y < HEIGHT:
                        if dfs(new_y, new_x, wordidx + 1):
                            return True
                seen.remove((x, y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j):
                        return True
        return False

        CAA
        AAA
        BCD
        

