# Runtime: 57 ms, faster than 94.69% of Python3 online submissions for Shuffle String.
# Memory Usage: 13.8 MB, less than 63.48% of Python3 online submissions for Shuffle String.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        table, ans = dict(), ''
        i =  j = 0
        while i < len(indices):
            table[indices[i]] = s[i]
            i += 1
            
        while j < len(indices):
            ans += table[j]
            j +=1
        return ans
            