class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
                     2 5 6

                        2                                                           []
        2.      5               6       []                      5                   6               []
        
    2.   
        
        
        '''
        ans = []
        def dfs(currtracked, start, total):
            if total == target:
                ans.append(currtracked.copy())
                return
            
            elif total > target:
                return
            
            for i in range(start, len(nums)):
                currtracked.append(nums[i])
                dfs(currtracked, i, total + nums[i])
                currtracked.pop()
        
        dfs([], 0, 0)
        return ans


            