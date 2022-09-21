# Runtime: 35 ms, faster than 92.71% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.8 MB, less than 95.99% of Python3 online submissions for Number of Good Pairs.

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)
        goodPairs = 0
        for num in count.keys():
            numPairs = count[num]*(count[num]-1)//2            
            goodPairs += numPairs
            
        return goodPairs
                
        