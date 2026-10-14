class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        WIDTH = len(grid[0])
        HEIGHT = len(grid)
        ACTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        seen = set()
        maxsize = 0

        def bfs(y, x):
            cursize = 0
            queue = deque()
            queue.append((y, x))
            seen.add((y, x))

            while queue:
                i,j = queue.popleft()
                cursize+=1

                for ay, ax in ACTIONS:
                    pot_y = ay + i
                    pot_x = ax + j

                    if pot_x >= 0 and pot_x < WIDTH and pot_y >= 0 and pot_y < HEIGHT and grid[pot_y][pot_x] == 1:
                        if (pot_y, pot_x) not in seen:
                            queue.append((pot_y, pot_x))
                            seen.add((pot_y, pot_x))
            
            return cursize

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == 1:
                    maxsize = max(maxsize, bfs(i,j))
        
        return maxsize

            




