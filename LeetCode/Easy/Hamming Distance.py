# Runtime: 27 ms, faster than 98.08% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13.8 MB, less than 64.23% of Python3 online submissions for Hamming Distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        num = 0
        while xor>0:
            xor = xor & (xor-1)
            num +=1
        return num
        