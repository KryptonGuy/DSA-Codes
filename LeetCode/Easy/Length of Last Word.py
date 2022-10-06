# Runtime: 49 ms, faster than 57.75% of Python3 online submissions for Length of Last Word.
# Memory Usage: 13.8 MB, less than 98.72% of Python3 online submissions for Length of Last Word.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        point = len(s)-1
        if s[point]==" ":
            while s[point]== " ":
                point -= 1
        start = point
        while point >= 0 and s[point]!=" ":
            point -= 1
        return start - point
        