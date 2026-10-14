class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(currlist, seen):
            if len(currlist) == len(nums):
                ans.append(currlist)
                return

            seencopy = seen.copy()

            for i in range(len(nums)):
                if nums[i] not in seencopy:
                    seencopy.add(nums[i])
                    dfs(currlist + [nums[i]], seencopy)
                    seencopy.remove(nums[i])
                
        dfs([], set())

        return ans

    '''
            curidx = 0, []
            i = 0
                curidx = 1, [1]
                i = 1
                    curidx = 2, [1 2]
                    i = 2
                        curidx = 3, [1 2 3]



                    1   2   3
                1               2               3
        12.         13.   21        23.      31.       32
        123.        132   213       231.     312.      321
    '''


            
        