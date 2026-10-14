class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int):
        self.stack.append(val)
        self.minStack.append(min(val, (self.minStack[-1] if len(self.minStack) >= 1 else val)))

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]




