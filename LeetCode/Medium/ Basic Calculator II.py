# Runtime: 74 ms, faster than 97.63% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.9 MB, less than 29.66% of Python3 online submissions for Basic Calculator II.

class Solution:
    def calculate(self, s: str) -> int:
        stack,pre_op = [], '+'
        num = 0
        s += '+'
        for l in s:
            if l.isdigit():
                num = num*10 + int(l)
            elif l == " ":
                continue
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    val = stack.pop()
                    stack.append(num*val)
                elif pre_op == '/':
                    val = stack.pop()
                    stack.append(int(val/num))
                
                num = 0
                pre_op = l
            
        return sum(stack)