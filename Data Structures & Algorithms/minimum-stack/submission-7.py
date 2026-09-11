class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = float("infinity")
        self.minValList = [self.minVal]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minValList.append(val)
        self.minValList.sort()
        self.minVal = self.minValList[0]

    def pop(self) -> None:
        self.minValList.remove(self.stack[-1])
        if self.stack and self.stack[-1] == self.minVal:
            self.minValList.sort()
            self.minVal = self.minValList[0]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal
