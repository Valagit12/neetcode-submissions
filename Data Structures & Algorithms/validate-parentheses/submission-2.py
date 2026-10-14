class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = '[{('
        closes = ']})'
        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if len(stack) > 0:
                    opener = stack[-1]
                else:
                    return False
                if opener == '[' and c == ']':
                    stack.pop()
                elif opener == '{' and c == '}':
                    stack.pop()
                elif opener == '(' and c == ')':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        