class MinStack:

    def __init__(self):
        self.cur_min = []
        # where first element is the first element added
        self.stack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.cur_min:
            self.cur_min.append(min(self.cur_min[-1], val))
        else: self.cur_min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.cur_min[-1]
        
