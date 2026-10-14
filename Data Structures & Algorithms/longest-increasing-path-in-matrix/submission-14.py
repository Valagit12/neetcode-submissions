class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''

            5   5   3

            2   3   6

            1   1   1

        '''

        seen = set()
        maxY = len(matrix)
        maxX = len(matrix[0])

        cache = {}

        actions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        cache = {}

        def dfs(y, x, lengthOfPath):
            num = matrix[y][x]

            if (y, x) in cache:
                return lengthOfPath + cache[(y, x)]

            curmax = lengthOfPath + 1

            for ax, ay in actions:
                pot_x = x + ax
                pot_y = y + ay

                if (
                    0 <= pot_x < maxX
                    and 0 <= pot_y < maxY
                    and num < matrix[pot_y][pot_x]
                ):
                    curmax = max(
                        dfs(pot_y, pot_x, lengthOfPath + 1),
                        curmax
                    )

            cache[(y, x)] = curmax - lengthOfPath
            return curmax

        ans = 0

        for i in range(maxY):
            for j in range(maxX):
                ans = max(ans, dfs(i, j, 0))

        return ans


            