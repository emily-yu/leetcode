class MinStack:

    def __init__(self):
        self.stk = []
        self.minval = 99999999999999999999

    def push(self, val: int) -> None:
        # minval check
        if val < self.minval:
            self.minval = val

        # add val to stack
        self.stk.append(val)
        print(self.stk)

    def pop(self) -> None:
        # minval check
        topelem = self.stk.pop()
        if topelem == self.minval:
            self.minval = 99999999999999999999
            for elem in self.stk:
                if elem < self.minval:
                    self.minval = elem
        print(topelem, self.stk)
        # return topelem

    def top(self) -> int:
        return self.stk[len(self.stk) - 1]

    def getMin(self) -> int:
        print(self.minval)
        if len(self.stk) == 0:
            return None
        return self.minval
