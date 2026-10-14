class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])


        ACTION = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque()
        seen = set()
        seenFresh = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    seenFresh.add((i,j))
        

        curTime = 0
        while queue:
            
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for ai, aj in ACTION:
                    pi, pj = i + ai, j + aj

                    if pi >= 0 and pi < ROWS and pj >= 0 and pj < COLS and (pi, pj) not in seen and grid[pi][pj] == 1:
                        seen.add((pi, pj))
                        seenFresh.remove((pi, pj))
                        queue.append((pi, pj))
            
            curTime += 1
        

        return -1 if len(seenFresh) else max(0, curTime - 1)



