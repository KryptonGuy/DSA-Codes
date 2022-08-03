from math import log10

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit = 0
        for num in nums:
            digit = int(math.log10(num)) + 1
            if digit%2 == 0:
                even_digit += 1
        return even_digit