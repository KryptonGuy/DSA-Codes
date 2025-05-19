class Solution:
    def triangleType(self, nums: List[int]) -> str:
        h = set(nums)
        if len(h)==1:
            return "equilateral"
        elif len(h)==2 and max(nums) < (sum(nums)-max(nums)):
            return "isosceles"
        elif len(h)==3 and max(nums) < (sum(nums)-max(nums)):
            return "scalene"
        else:
            return "none"