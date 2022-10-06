# Runtime: 277 ms, faster than 59.58% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.3 MB, less than 74.89% of Python3 online submissions for Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev,i = False, 0
        flowerbed.append(0)
        while i < len(flowerbed)-1 and n != 0:
            if flowerbed[i] ==1:
                prev = True
            else:
                if not prev and flowerbed[i+1]==0:
                    n -=1
                    prev = True
                else:
                    prev = False
            i += 1
        return n ==0
                
        