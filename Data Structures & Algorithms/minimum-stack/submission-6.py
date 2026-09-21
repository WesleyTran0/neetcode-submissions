class MinStack:

    def __init__(self):
        self.minStack = []
        self.curStack = []
        

    def push(self, val: int) -> None:
        self.curStack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        self.curStack.pop()

    def top(self) -> int:
        return self.curStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
