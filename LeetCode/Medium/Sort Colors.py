# Runtime: 57 ms, faster than 66.22% of Python3 online submissions for Sort Colors.
# Memory Usage: 13.9 MB, less than 63.96% of Python3 online submissions for Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i , j = 0 , 0
        
        while j < len(nums):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
            j += 1
        
        j = i
        
        while j < len(nums):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
            j += 1
            
        j = i
        
        while j < len(nums):
            if nums[j] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                i +=1
            j += 1
        
    