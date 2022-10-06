# Runtime: 25 ms, faster than 99.63% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
# Memory Usage: 13.8 MB, less than 95.58% of Python3 online submissions for Substrings of Size Three with Distinct Characters.

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count,h = 0,3        
        while h < len(s)+1:
            if len(set(s[h-3:h]))==3:
                count += 1 
            h +=1
        return count