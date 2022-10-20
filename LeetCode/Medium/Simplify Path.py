# Runtime: 45 ms, faster than 75.86% of Python3 online submissions for Simplify Path.
# Memory Usage: 13.9 MB, less than 80.37% of Python3 online submissions for Simplify Path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk= []
        path = path.replace('//','/').rstrip('/')
        for string in path.split('/'):
            if string=='.' or len(string)==0:
                continue
            elif string == '..':
                if len(stk)==0:
                    continue
                else:
                    stk.pop()
            else:
                stk.append(string)
        return '/'+'/'.join(stk)
            
            
            