class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        ans = []


        def backtracking(openN, closedN):
            if openN == closedN == n:
                ans.append(''.join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtracking(openN+1, closedN)
                print(1,''.join(stack))
                stack.pop()
                
            if openN > closedN:
                stack.append(')')
                backtracking(openN, closedN+1)
                print(2, ''.join(stack))
                stack.pop()
            
        
        backtracking(0, 0)
        return ans



                 

