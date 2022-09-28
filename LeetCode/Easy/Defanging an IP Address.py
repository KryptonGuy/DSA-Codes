# Runtime: 28 ms, faster than 96.95% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14 MB, less than 5.84% of Python3 online submissions for Defanging an IP Address.


class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = '' 
        for letter in address:
            if letter=='.':
                ans += "[.]"
                continue
            ans += letter
        
        return ans
        