class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcon = 0
        max = 0

        for num in nums:
            if num==0:
                max = 0
            if num==1:
                max += 1
            if max> maxcon:
                maxcon = max
            
        return maxcon