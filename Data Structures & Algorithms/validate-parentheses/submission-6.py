class Solution:
    def bracketsMatch(self, c1: chr, c2: chr) -> bool:
        square = '[]'
        curl = '{}'
        brack = '()'

        if not c1 == c2:
            if (c1 in square and c2 in square or
                c1 in curl and c2 in curl or
                c1 in brack and c2 in brack):
                return True
        return False


    def isValid(self, s: str) -> bool:
        open_brackets = '([{'

        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
            elif stack and self.bracketsMatch(c, stack[-1]):
                stack.pop()
            else: return False
        

        if len(stack) == 0:
            return True
        else:
            return False
                