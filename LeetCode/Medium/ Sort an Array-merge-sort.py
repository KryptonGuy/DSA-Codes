# Runtime: 1703 ms, faster than 43.68% of Python3 online submissions for Sort an Array.
# Memory Usage: 22.7 MB, less than 29.71% of Python3 online submissions for Sort an Array.


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:        
        if len(nums)<2:
            return nums
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.combine(left, right)
            
    def combine(self, left, right):
        
        i,j = 0, 0
        ans = []
        
        while i < len(left) and j < len(right):
            
            if left[i]<right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        
        if (i == len(left)):
            ans.extend(right[j:])
        else:
            ans.extend(left[i:])
        
        return ans
            
        
        