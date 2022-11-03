# Runtime: 37 ms, faster than 88.36% of Python3 online submissions for Minimum Bit Flips to Convert Number.
# Memory Usage: 13.8 MB, less than 62.15% of Python3 online submissions for Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        
        num = 0
        
        while xor>0:
            xor = xor & (xor-1)
            num += 1
            
        return num
        
        