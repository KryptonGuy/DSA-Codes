# Runtime: 50 ms, faster than 66.03% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.9 MB, less than 15.12% of Python3 online submissions for XOR Operation in an Array.

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i, arr = 1, [None]*n
        xor = start
        arr[0] = start
        
        while i < n:
            nu = start + (2*i)
            xor = xor ^ nu
            arr[i] = nu
            i += 1
        return xor
            
        