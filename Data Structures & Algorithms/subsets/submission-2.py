class Solution:   

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(index):
            if index >= len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)
            
        dfs(0)
        return ans

        '''

            [1].                        []
        
        [1 2]       [1]             [2].     []
     
    [1 2 3] [1 2] [1 3]. [3].    [2 3] [2]. [3]. []


        '''
