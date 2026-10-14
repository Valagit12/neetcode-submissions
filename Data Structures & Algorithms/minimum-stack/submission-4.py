class MinStack:

    def __init__(self):
        self.minstack = []
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.minstack) > 0:
            currmin = self.minstack[-1]
            self.minstack.append(min(currmin, val))
            self.stack.append(val)
            return

        self.minstack.append(val)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

'''
1 2
1 1

'''
        
