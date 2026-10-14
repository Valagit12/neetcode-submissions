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
            if sum(currtracked) == target:
                ans.append(currtracked)
                return
            
            elif sum(currtracked) > target:
                return
            
            dfs(currtracked + [nums[start]], start, total + nums[start])
            for i in range(start+1, len(nums)):
                dfs(currtracked + [nums[i]], i, total + nums[i])
        
        dfs([], 0, 0)
        return ans


            