class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = 0
        odd = len(nums) -1
        
        while even < odd:
            if nums[even]%2 == 0:
                even += 1
                continue
            elif nums[odd]%2 == 1:
                odd -= 1
                continue
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                
        return nums