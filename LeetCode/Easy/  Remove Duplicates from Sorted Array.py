class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        size = len(nums)
        
        while i < size-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                size -= 1
            else:
                i += 1