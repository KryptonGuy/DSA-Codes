# Runtime: 40 ms, faster than 94.02% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.8 MB, less than 64.31% of Python3 online submissions for Kids With the Greatest Number of Candies.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = [None] * len(candies)
        
        for i in range(len(candies)):
            if (candies[i]+extraCandies) >= maxCandies:
                result[i] = True
            
            else:
                result[i] = False
                
        return result
        
        