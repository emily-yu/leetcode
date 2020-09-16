#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_val = None

    def push(self, x: int) -> None:
        # self.print()
        self.data.append(x)

        # assign min_val if not assigned
        if (self.min_val is None):
            self.min_val = x
        # reassign min_val if new val is new min_val
        elif (self.min_val > x):
            self.min_val = x

    def pop(self) -> None:
        # self.print()
        x = self.data.pop()
        # print("asdf")
        # print(x)
        # print(self.data)
        # pop and there could be nothing left
        if len(self.data) == 0:
            self.min_val = None
        # pop and the element popped could be the min, need to reset
        elif x == self.min_val:
            self.min_val = min(self.data)
        # pop no special element
        # print(self.min_val)
        # print(self.getMin())

    def top(self) -> int:
        # self.print()

        # if there still exists data, return top
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    def getMin(self) -> int:
        # self.print()
        return self.min_val
    
    def print(self) -> None:
        # print(self.data)
        pass


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(2)
# obj.print()
# obj.pop()
# obj.print()

# param_3 = obj.top()
# param_4 = obj.getMin()
# print(param_3)
# print(param_4)
# @lc code=end

