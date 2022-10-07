# Runtime: 361 ms, faster than 28.18% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.
# Memory Usage: 14.6 MB, less than 98.84% of Python3 online submissions for Partitioning Into Minimum Number Of Deci-Binary Numbers.

class Solution:
    def minPartitions(self, n: str) -> int:
        maxnum = 0
        for num in n:
            maxnum = max(maxnum, int(num))
        return maxnum
            
        