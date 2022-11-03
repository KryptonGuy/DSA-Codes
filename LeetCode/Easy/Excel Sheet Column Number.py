# Runtime: 47 ms, faster than 76.00% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.8 MB, less than 55.84% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i, ans = len(columnTitle)-1, 0
        while i > -1:
            ans += ((26**(len(columnTitle)-i-1)) * (ord(columnTitle[i]) -64))
            i -=1
        return ans
        