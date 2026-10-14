class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        The key insight to this problem is to recognize that you make decisions when a star exists

        Assume we had:
        xyz
        i
        .*z
        j

        Here, we should check if the next j element is a * because that requires alternative decisions
        Since it is a * and '.' and 'x' match, then we could either not use the * or use the *
        so either move on to the subproblems
            (i + 1, j) -> use the star, so increment i by one and keep j where it is incase you want to use . again.
            (i, j + 2) -> do not use the star, increment j by two to skip the star and move on to the next character
        For our current case, we know that the correct path is to use the star, but we would have to try both options in code to know for certain

        Then we would have i = y and j = ., and we would use the star again

        Now, i = z and j = . so we could use the * again but if we go down this decision, i will come to the end and j will stay at .
            That means that there would be no match between . and i being at the end, so, we could only move on to subproblem (i, j + 2)
            Again there is no match, but now with this subproblem, there is also no *, so we have gotten to the end of i, with more pattern left and no *
            This means that the last decision we made was wrong and we have to backtrack
        
        We now backtrack and instead of using the * again, we skip it. and work on subproblem where i = z and j = z
            This is a simple match so we can increment both pointers which will lead to when both i and j are out of bounds 
            That means we have found a match so we can return True
        
        now quickly consider this problem
        aa a -> aa  a , here we can tell that i is in bounds but j is out of bounds, there is clearly no match. This is a base case
        i  j     i   j

        We saw the alternative above, where i is out of bounds but j is in bounds. It is still possible to have a match via a star. We could form
        a base case with that but that would be messy and unnecessary since our pointer increments would just handle it.

        Finally, we can use DP to optimize the problem and remove redundant checks.
        '''

        dp = {}

        def dfs(str_ptr, pat_ptr):
            if (str_ptr, pat_ptr) in dp:
                return dp[(str_ptr, pat_ptr)]
            if str_ptr >= len(s) and pat_ptr >= len(p):
                return True
            if pat_ptr >= len(p): # The edge case above, is str_ptr is still in bounds but pat_ptr is out of bounds, there is no solution
                return False
            
            # If the two characters match
            match = str_ptr < len(s) and (s[str_ptr] == p[pat_ptr] or p[pat_ptr] == '.')

            # Now we must handle if the next character in the pattern is a star
            if pat_ptr + 1 < len(p) and p[pat_ptr + 1] == '*':
                if match:
                    dp[(str_ptr, pat_ptr)] = ( # If there is a match and the next character is a *, then
                        dfs(str_ptr + 1, pat_ptr) or #we can either use the star
                        dfs(str_ptr, pat_ptr + 2) #or skip the star. If either of these two calls return True, then we have a True
                    )
                else:
                    dp[(str_ptr, pat_ptr)] = dfs(str_ptr, pat_ptr + 2) # If there is no match, then all we can do is skip the *
            elif match:
                # If there is no star but a match, all we need do is move on to the next indices
                dp[(str_ptr, pat_ptr)] = dfs(str_ptr + 1, pat_ptr + 1)
            else:
                # If there is no star and no match, then there is no match between the pattern and the string for the current subproblem
                dp[(str_ptr, pat_ptr)] = False
            return dp[(str_ptr, pat_ptr)]
        
        return dfs(0, 0)




















