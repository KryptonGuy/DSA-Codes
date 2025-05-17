class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num1,num2,num3 =0,0,0
        for num in nums:
            if num==0:
                num1 += 1
            elif num==1:
                num2+= 1
            else:
                num3 += 1
        i = 0
        while num1:
            nums[i] = 0
            i += 1
            num1 -= 1
        while num2:
            nums[i] = 1
            i += 1
            num2 -= 1
        while num3:
            nums[i] = 2
            i += 1
            num3 -= 1


        