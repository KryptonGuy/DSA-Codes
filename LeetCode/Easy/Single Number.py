# Runtime: 175 ms, faster than 81.86% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 84.26% of Python3 online submissions for Single Number.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for num in nums[1:]:
            xor = xor ^ num
        return xor