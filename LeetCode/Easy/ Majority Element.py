# Runtime: 165 ms, faster than 97.90% of Python3 online submissions for Majority Element.
# Memory Usage: 15.6 MB, less than 34.29% of Python3 online submissions for Majority Element.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]