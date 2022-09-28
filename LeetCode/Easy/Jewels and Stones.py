# Runtime: 37 ms, faster than 85.19% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 14 MB, less than 11.76% of Python3 online submissions for Jewels and Stones.

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                count +=1
        return count
        