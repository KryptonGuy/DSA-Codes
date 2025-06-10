class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)

        odd, even = float('-inf'),float('inf')
        for key, value in count.items():
            if value % 2==0:
                even = min(even,value)
            else:
                odd = max(odd,value)
        return odd - even



        