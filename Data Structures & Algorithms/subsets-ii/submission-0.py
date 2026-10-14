class Solution:
    # Since n < 20, Im assuming the solution should be 2^n or n!. Backtracking or brute force algorithm. Ik its backtracking but yk

    '''
            1 2 1

            Mathematically speaking, this problem is referring to the generation of all multisets.

            The number of solutions depends on the multiplicity of each unique element in the set.

            For this, the number of possible submultisets would be (2+1)(1+1)
            (2 + 1) - because you can take 1 anywhere from 0 to 2 times
            (1 + 1) - because you cantake 2 anywhere from 0 to 1 times.
            
            Approach it the way we approach generating all possible subsequences.
                            1                                               []
            2                               [].                  2                      []
        1.      []                      1.       []         1          []           1          []
       121.    12                      11.        1         21.        2.           1.          []
    
    Here 12 and 21 is duplicated

                                                                12144
                                        1                                                                   []
                    2                   []                                                  2                             []
            1.          []          1.          []                                    1.          []                1.          [] 
        4     [].    4.   []      4      [].    4.   []                              4     [].    4.   []         4     [].    4.   []
    4   [].  4. []. 4. [] 4 []   4  []. 4. []. 4. [] 4 []                        4   []. 4. []. 4. [] 4 []    4  [].  4. []. 4. [] 4 []
    1.  1.   1.  1. 1. 1. 1. 1.  1.  1. 1   1. 1.  1.1  []                       2.  2.   2.  2. 2. 2. 2. 2.  1.  1  1.  1. 4.  4 4
    2.  2.   2.  2. 2. 2. 2. 2.  1.  1  1.  1. 4.  4 4                           1.  1.   1.  1. 4. 4. 4.     4.  4. 4.     4
    1.  1.   1.  1. 4. 4. 4.     4.  4. 4.     4                                 4.  4.   4      4.           4
    4.  4.   4      4.           4.     x.           x                           4.  
    4.       x.           x.                                                     x.  x.   x.  x        x.     x.  x. x.  x.        x

    12144, 1214, 121, 1244, 124, 12, 1144, 114, 11, 144, 14, 1
    '''

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        nums.sort()

        def dfs(idx, seen):
            if idx >= len(nums):
                ans.append(seen)
                return
            
            dfs(idx + 1, seen + [nums[idx]])
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx+=1

            dfs(idx + 1, seen)
        
        dfs(0, [])

        return ans
            


