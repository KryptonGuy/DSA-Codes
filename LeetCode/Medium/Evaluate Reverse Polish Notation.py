# Runtime: 66 ms, faster than 96.96% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.3 MB, less than 95.77% of Python3 online submissions for Evaluate Reverse Polish Notation.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1+val2)
            elif tok == '*':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1*val2)
            elif tok == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
            elif tok == '/':
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
            else:
                stack.append(int(tok))

        return stack[0]
        