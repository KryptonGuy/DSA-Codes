# Runtime: 205 ms, faster than 44.06% of Python3 online submissions for Divide Array Into Equal Pairs.
# Memory Usage: 14.1 MB, less than 63.31% of Python3 online submissions for Divide Array Into Equal Pairs.
import collections

i
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        for s in count.keys():
            if count[s]%2!=0:
                return False
            
        return True
            
