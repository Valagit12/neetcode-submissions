class Solution:   

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(index, currans):
            if index == len(nums):
                ans.append(currans)
                return
            
            dfs(index + 1, currans + [nums[index]])
            dfs(index + 1, currans)
            
        dfs(0, [])
        return ans

        '''

            [1].                        []
        
        [1 2]       [1]             [2].     []
     
    [1 2 3] [1 2] [1 3]. [3].    [2 3] [2]. [3]. []


        '''
