class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''
        PACIFIC = {00, 10, 20, 30, 40, 01, 02}
        ATLANTIC = {02, 12, 32, 42, 52 51, 50}
        '''
        ACTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        queueP = deque()
        queueA = deque()
        
        for c in range(COLS):
            pacific.add((0, c))
            queueP.append((0, c))
            atlantic.add((ROWS - 1, c))
            queueA.append((ROWS - 1, c))
        for r in range(ROWS):
            pacific.add((r, 0))
            queueP.append((r, 0))
            atlantic.add((r, COLS - 1))
            queueA.append((r, COLS - 1))
        
        while queueP or queueA:
            for _ in range(len(queueP)):
                i, j = queueP.popleft()

                for ai, aj in ACTIONS:
                    pi, pj = ai + i, aj + j

                    if (pi >= 0 and pi < ROWS and pj >=0 and pj < COLS and (pi, pj) not in pacific
                        and heights[pi][pj] >= heights[i][j]):
                        pacific.add((pi, pj))
                        queueP.append((pi, pj))

            for _ in range(len(queueA)):
                i, j = queueA.popleft()

                for ai, aj in ACTIONS:
                    pi, pj = ai + i, aj + j

                    if (pi >= 0 and pi < ROWS and pj >=0 and pj < COLS and (pi, pj) not in atlantic
                            and heights[pi][pj] >= heights[i][j]):
                        atlantic.add((pi, pj))
                        queueA.append((pi, pj))

        ans = []

        for i in range(ROWS):
            for j in range(COLS):  
                if (i, j) in atlantic and (i,j) in pacific:
                    ans.append([i, j])
        return ans



       
        