# Runtime: 180 ms, faster than 99.96% of Python3 online submissions for Largest Perimeter Triangle.
#Memory Usage: 15.5 MB, less than 45.85% of Python3 online submissions for Largest Perimeter Triangle.
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        while i >1:
            if nums[i]<nums[i-1] + nums[i-2]:
                return sum(nums[i-2:i+1])
            i -=1
        return 0
            
        