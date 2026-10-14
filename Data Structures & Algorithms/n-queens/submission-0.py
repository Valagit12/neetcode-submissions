class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        '''  

                seen   
        Q...   (0, 0) -> covered.
        ..Q.   (1, 2)-> covered
        ....
        ....
        '''


        ans = []
        seenQueens = set()

        def valid(i, j):
            for qi, qj in seenQueens:
                if qj == j:
                    return False
                
                if qi - qj == i - j or qi + qj == i + j:
                    return False
                
            return True



        def dfs(row, currsoln):
            if row == n:
                ans.append(currsoln)
                return
            
            for j in range(n):
                if valid(row, j):
                    seenQueens.add((row, j))
                    dfs(row +1, currsoln +  [j*'.' + 'Q' + '.' * (n - j-1)])
                    seenQueens.remove((row, j))
        
        dfs(0, [])

        return ans










                    