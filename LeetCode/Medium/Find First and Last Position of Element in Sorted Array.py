# Runtime: 174 ms, faster than 20.90% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 47.76% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = 0, len(nums)-1
        while l<=h:
            mid = (h + l)//2
            
            if nums[mid]==target:
                inner = []
                while mid>= 0 and nums[mid]==target: mid -=1  
                inner.append(mid+1)
                mid += 1

                while mid<len(nums) and nums[mid]==target: mid +=1
                inner.append(mid-1)
                return inner
            
            elif nums[mid]> target: h = mid - 1
            else: l = mid +1    
        return [-1, -1 ]