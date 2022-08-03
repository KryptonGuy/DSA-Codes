class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        back = 0
        
        for forward in range(len(nums)):
            if nums[forward] != val:
                nums[back] = nums[forward]
                back += 1
                
        return back