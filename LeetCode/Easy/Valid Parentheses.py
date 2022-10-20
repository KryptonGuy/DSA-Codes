# Runtime: 56 ms, faster than 46.93% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 98.07% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stk, table = [], {'(':')', '{':'}','[':']'}
        for b in s:
            if b in table.keys():
                stk.append(b)
            else:
                if len(stk)==0:
                    return False
                else:
                    if b==table[stk.pop()]:
                        continue
                    else:
                        return False
        return len(stk)==0