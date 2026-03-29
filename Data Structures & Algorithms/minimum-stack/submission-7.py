class MinStack:
    # self would be a 
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

        

    def pop(self) -> None:
        pop1 = self.stack.pop()
        if pop1 == self.minStack[-1]:
            self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # we get the min of the stack
        return self.minStack[-1]
        
