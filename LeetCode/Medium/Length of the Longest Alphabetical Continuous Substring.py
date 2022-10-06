# Runtime: 1080 ms, faster than 43.33% of Python3 online submissions for Length of the Longest Alphabetical Continuous Substring.
# Memory Usage: 14.9 MB, less than 59.46% of Python3 online submissions for Length of the Longest Alphabetical Continuous Substring.


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest, j = 0 , 0
        lent = len(s)
        while j <lent:
            tracer = 1
            while j <lent-1 and ord(s[j]) +1==ord(s[j+1]):
                tracer +=1
                j += 1
            if tracer > longest:
                longest = tracer
            j +=1
        return longest
                
                
        
        