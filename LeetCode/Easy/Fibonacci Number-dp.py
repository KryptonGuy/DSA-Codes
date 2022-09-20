# Runtime: 46 ms, faster than 69.56% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 13.9 MB, less than 9.47% of Python3 online submissions for Fibonacci Number.


class Solution:
    hashtable = {}
    def fib(self, n: int) -> int:
        try:
            return self.hashtable[n]
        except:
            pass
            
        if n==0:
            return 0
        if n==1:
            return 1
        
        su = self.fib(n-1) + self.fib(n-2)
        
        self.hashtable[n] = su
        
        return su
        