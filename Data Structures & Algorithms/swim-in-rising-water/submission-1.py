class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        0   1   2   3   4
        24  23  22  21  5
        0   15  15  15  16
        0   0   18  19  20
        0   0   0   0   0
        
        not in seen
        max(parDist, childValue)
        '''

        ACTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        # Each element is stored by pathTime, i, j
        minheap = [(grid[0][0], 0, 0)]
        seen = set()

        while minheap:
            pathTime, i, j = heapq.heappop(minheap)

            if (i, j) in seen:
                continue
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return pathTime
            
            seen.add((i, j))

            for ai, aj in ACTIONS:
                pot_i, pot_j = ai + i, aj + j
                if pot_i >= 0 and pot_i < len(grid) and pot_j >= 0 and pot_j < len(grid[0]) and (pot_i, pot_j) not in seen:
                    heapq.heappush(minheap, ( max(pathTime, grid[pot_i][pot_j]),pot_i, pot_j))
            
        

        
