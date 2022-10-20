# Runtime: 571 ms, faster than 96.29% of Python3 online submissions for Increasing Triplet Subsequence.
# Memory Usage: 24.7 MB, less than 48.78% of Python3 online submissions for Increasing Triplet Subsequence.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        one = two = float('inf')
        for num in nums:
            if num>two>one:
                return True
            elif num<=one:
                one = num
            elif num<=two:
                two = num
            
        
        return False
                
            
        