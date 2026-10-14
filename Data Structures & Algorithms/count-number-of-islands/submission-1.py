class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0

        WIDTH = len(grid[0])
        HEIGHT = len(grid)
        ACTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque()

            queue.append((i, j))

            while queue:
                y, x = queue.popleft()

                if (y,x) not in seen:
                    seen.add((y, x))
                    for ay, ax in ACTIONS:
                        if 0<= y+ay and HEIGHT > y + ay and 0 <= x+ax and WIDTH > x + ax and grid[y+ay][x+ax] == '1':
                            queue.append((y+ay, x+ax))

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if grid[i][j] == '1' and (i, j) not in seen:
                    count += 1
                    bfs(i, j)
        
        return count
        

        