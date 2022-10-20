# Runtime: 64 ms, faster than 92.35% of Python3 online submissions for Min Stack.
# Memory Usage: 18.8 MB, less than 6.42% of Python3 online submissions for Min Stack.

class MinStack:

    def __init__(self):
        self.stk = []   

    def push(self, val: int) -> None:
        if len(self.stk)==0:
            self.stk.append([val, val])
        else:
            self.stk.append([val,min(self.stk[-1][1], val)])
            
    def pop(self) -> None:
        pop = self.stk[-1][0]
        del self.stk[-1]
        return pop

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()