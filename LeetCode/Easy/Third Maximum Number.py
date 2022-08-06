class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        one= -float('inf')
        two= -float('inf')
        three= -float('inf')
        
        for num in nums:
            if num == one or num == two or num == three:
                continue
                
            if num > one:
                three = two
                two = one
                one = num
                
            elif num > two:
                three = two
                two = num
                
            elif num > three:
                three = num
        
        if three == -float('inf'):
            return one

        return three
                