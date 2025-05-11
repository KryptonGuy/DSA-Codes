class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        some = 0
        for num in arr:
            if num % 2==1:
                some += 1
            else:
                some = 0
            if some==3:
                return True
            
        return False
