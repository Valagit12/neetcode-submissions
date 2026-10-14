class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        ACTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        seen = set()
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):

                if grid[i][j] == 0:
                    queue.append((i,j))
                    seen.add((i, j))

        currDistance = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for ai, aj in ACTIONS:
                    pot_i, pot_j = i + ai, j + aj

                    if (pot_i >= 0 and pot_i < ROWS and pot_j >= 0 and pot_j < COLS and (pot_i, pot_j) not in seen
                        and grid[pot_i][pot_j] != -1):
                        grid[pot_i][pot_j] = currDistance + 1
                        seen.add((pot_i, pot_j))
                        queue.append((pot_i, pot_j))
            
            currDistance += 1



