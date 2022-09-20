# Runtime: 66 ms, faster than 11.96% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.7 MB, less than 97.50% of Python3 online submissions for Pow(x, n).

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, abs(n))
        elif n==0:
            return 1
        elif n%2==0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(x, n-1)*x
