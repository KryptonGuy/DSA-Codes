# Runtime: 280 ms, faster than 91.44% of Python3 online submissions for First Missing Positive.
# Memory Usage: 31.3 MB, less than 49.61% of Python3 online submissions for First Missing Positive.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
                
        counts = collections.Counter(nums)
        for i in range(1,len(nums)+1):
            if counts[i]==0:
                return i
            
        return i +1