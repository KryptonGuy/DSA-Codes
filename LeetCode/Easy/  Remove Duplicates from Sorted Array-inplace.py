class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for j in range(len(nums)-1):
            if nums[j] == nums[j+1]:
                continue
            nums[i] = nums[j]
            i += 1
        nums[i] = nums[-1]
        
        return i+1
        
         
            
    