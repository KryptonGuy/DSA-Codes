# Runtime: 88 ms, faster than 75.36% of Python3 online submissions for Palindrome Number.
# Memory Usage: 13.9 MB, less than 59.05% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        ss = str(x)
        return ss==ss[::-1]
        
        