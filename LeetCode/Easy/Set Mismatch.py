# Runtime: 240 ms, faster than 83.25% of Python3 online submissions for Set Mismatch.
# Memory Usage: 15.8 MB, less than 41.20% of Python3 online submissions for Set Mismatch.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = dict()
        for num in nums:
            if num in counter:
                dup = num
            counter[num] = True
        
        for i in range(1,len(nums)+1):
            if i not in counter:
                nahi = i
                break
        return [dup, nahi]