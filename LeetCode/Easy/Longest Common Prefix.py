# Runtime: 34 ms, faster than 95.60% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14 MB, less than 11.72% of Python3 online submissions for Longest Common Prefix.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest,i = strs[0],1
        
        for i in range(1,len(strs)):
            j = 0
            while j < len(longest) and j <len(strs[i]) and strs[i][j]==longest[j]:
                j += 1
            
            longest = strs[i][:j]
            
        return longest
            
        