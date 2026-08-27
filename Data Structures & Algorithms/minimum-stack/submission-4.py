class MinStack:
    def __init__(self):
        self.curSelf = []
        self.curMins = []
        

    def push(self, val: int) -> None:
        self.curSelf.append(val)
        if not self.curMins or val < self.curMins[-1]:
            self.curMins.append(val)
        else:
            self.curMins.append(self.curMins[-1])

    def pop(self) -> None:
        self.curSelf.pop()
        self.curMins.pop()

    def top(self) -> int:
        return self.curSelf[-1]

    def getMin(self) -> int:
        return self.curMins[-1]
        
