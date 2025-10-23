class SpecialStack:
    def __init__(self):
        # main stack to store elements
        self.stack = []
        # auxiliary stack to store minimum elements
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        # If min_stack is empty or x is smaller/equal to current min, push x to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        # If popped element is the current minimum, pop from min_stack as well
        if top == self.min_stack[-1]:
            self.min_stack.pop()

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
