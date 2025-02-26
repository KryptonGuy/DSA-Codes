class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        maxsum, res, minsum, i = 0, 0, 0, 0

        while i < len(nums):
            if maxsum + nums[i] > 0:
                maxsum += nums[i]
            else:
                maxsum = 0
            
            if minsum + nums[i] < 0:
                minsum += nums[i]
            else:
                minsum = 0
            
            res = max(res, maxsum, -(minsum))

            i += 1

        return res
