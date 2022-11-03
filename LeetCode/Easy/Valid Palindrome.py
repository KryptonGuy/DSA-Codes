# Runtime: 73 ms, faster than 73.98% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 85.58% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        dul = ''
        for char in s:
            if char.isalnum():
                dul += char.lower()
        i , j = 0 , len(dul)-1
        

        while i <=j:
            if dul[i]== dul[j]:
                i +=1
                j -=1
            else:
                return False
        return True
        