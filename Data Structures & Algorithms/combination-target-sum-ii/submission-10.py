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
                return

            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if (i > start and candidates[i] == candidates[i-1]):
                    continue
                if total > candidates[i] + target:
                    return
                currtracked.append(candidates[i])
                dfs(currtracked, i+1, total + candidates[i])
                currtracked.pop()

        dfs([], 0, 0)
        return ans   