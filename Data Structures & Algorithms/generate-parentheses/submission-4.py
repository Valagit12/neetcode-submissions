class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = 3
                            (
                        (.         )
                    (.     )     (   
                    )   (    )  ( )  
                    )   ).   (. ) (
                    )   ).   ). ) )


                            (
                        (.       )
                    (.     ).  (.     )
                    x.    ( ) (  ).   x
                          x.  x.     


                           (
                          (. )
                          x
        '''              

        ans = [] 

        def dfs(num_starts, num_closes, currstring):
            if len(currstring) == 2*n:
                ans.append(currstring)
                return

            if num_starts < n:
                dfs(num_starts + 1, num_closes, currstring + '(')
            if num_closes < num_starts:
                dfs(num_starts, num_closes + 1, currstring + ')')
        dfs(0, 0, '')
        return ans


