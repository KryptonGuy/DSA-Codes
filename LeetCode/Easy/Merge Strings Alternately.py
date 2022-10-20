# Runtime: 43 ms, faster than 76.22% of Python3 online submissions for Merge Strings Alternately.
# Memory Usage: 13.9 MB, less than 20.03% of Python3 online submissions for Merge Strings Alternately.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = ''
        while i < len(word1) and j < len(word2):
            ans += word1[i]
            ans += word2[j]
            i += 1; j += 1
            
        if i < len(word1):
            ans += word1[i:]
        elif j < len(word2):
            ans += word2[j:]
            
        return ans
        