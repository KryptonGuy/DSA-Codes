class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        @cache
        def power(x,k):
            if k ==0:
                return 1
            if k == 1:
                return x

            if (k % 2)==0:
                return (power(x, k//2) * power(x,k//2)) % mod
            else:
                return (x * power(x, k//2) * power(x,k//2)) % mod

        if n % 2==0:
            ans = ((power(5,n//2))*(power(4,n//2)) % mod)
        else:
            ans = ((power(5,n//2 + 1))*(power(4,n//2)) % mod)

        return ans
