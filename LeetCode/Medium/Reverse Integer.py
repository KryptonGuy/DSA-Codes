# Runtime: 56 ms, faster than 47.36% of Python3 online submissions for Reverse Integer.
# Memory Usage: 14 MB, less than 16.60% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        ans, neg = 0, False
        if x <0:
            neg = True
        x = abs(x)
        while x > 0:  
            ans *= 10    
            ans += abs(x) % 10      
            x = x // 10   
        if ans > 2**31: return 0      
        if neg: ans *= -1      
        return ans
  