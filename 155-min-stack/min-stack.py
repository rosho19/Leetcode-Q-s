class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # use extra space to create a stack that stores min value at the top 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not bool(self.min_stack):
            self.min_stack.append(val)
        elif val < self.min_stack[-1]: # only push new val if it's less than current minimum
            self.min_stack.append(val)
        else: self.min_stack.append(self.min_stack[-1]) # Push current minimum value again

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not bool(self.stack): # ensures no error for out of range
            return null
        return self.stack[-1]

    def getMin(self) -> int:
        if not bool(self.min_stack):
            return null
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()