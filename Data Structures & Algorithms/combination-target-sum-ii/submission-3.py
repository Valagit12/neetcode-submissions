class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []

        candidates.sort()
        def dfs(currtracked, start, total):
            if total == target:
                ans.append(currtracked.copy())

            elif total > target:
                return

            seen = set()
            for i in range(start, len(candidates)):
                if candidates[i] not in seen:
                    seen.add(candidates[i])
                    currtracked.append(candidates[i])
                    dfs(currtracked, i+1, total + candidates[i])
                    currtracked.pop()

        dfs([], 0, 0)
        return ans   