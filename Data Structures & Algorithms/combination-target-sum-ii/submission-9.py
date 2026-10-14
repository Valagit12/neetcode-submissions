class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        1 1 2 5 6 7 10
        
        1
    

        '''

        ans = []

        candidates.sort()
        def dfs(currtracked, start, total):
            if total == target:
                ans.append(currtracked.copy())

            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if (i > start and candidates[i] == candidates[i-1]) or total + candidates[i] > target:
                    continue
                currtracked.append(candidates[i])
                dfs(currtracked, i+1, total + candidates[i])
                currtracked.pop()

        dfs([], 0, 0)
        return ans   