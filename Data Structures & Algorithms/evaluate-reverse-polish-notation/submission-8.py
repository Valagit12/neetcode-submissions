class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '/', '*'}
        for tok in tokens:
            if tok in operations:
                if tok == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tok == '*':
                    stack.append(stack.pop() * stack.pop())
                elif tok == '/':
                    first,second = stack.pop(), stack.pop()
                    print(first, second)
                    done = second / first
                    stack.append(int(done))
                elif tok == '-':
                    stack.append(-1 * (stack.pop() - stack.pop()))
            else:
                stack.append(int(tok))

        return stack[0]
                
