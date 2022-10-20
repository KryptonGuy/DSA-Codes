# Runtime: 65 ms, faster than 66.72% of Python3 online submissions for Baseball Game.
# Memory Usage: 14.1 MB, less than 75.17% of Python3 online submissions for Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            try:
                stk.append(int(op))
            except:
                if op=="+":
                    stk.append(stk[-1]+stk[-2])
                elif op=='D':
                    stk.append(stk[-1]*2)
                else:
                    stk.pop()
        
        return sum(stk)