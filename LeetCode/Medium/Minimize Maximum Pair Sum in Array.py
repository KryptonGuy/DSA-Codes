# Runtime: 1258 ms, faster than 94.05% of Python3 online submissions for Minimize Maximum Pair Sum in Array.
# Memory Usage: 27.8 MB, less than 70.63% of Python3 online submissions for Minimize Maximum Pair Sum in Array.

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0, len(nums)-1
        maxcount = 0
        while i<j:
            maxcount = max(maxcount, (nums[i]+nums[j]))
            i +=1
            j -=1
        
        return maxcount