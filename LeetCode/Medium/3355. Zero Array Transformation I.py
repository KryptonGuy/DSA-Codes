class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # for q in queries:
        #     for i in range(q[0], q[1]+1):
        #         nums[i] -= 1
            
        # for num in nums:
        #     if num>0:
        #         return False
        # return True

        deltaArry = [0] * (len(nums) + 1)

        for l, r in queries:
            deltaArry[l] += 1
            deltaArry[r+1] -= 1
        total = []
        curr = 0

        for num in deltaArry:
            curr += num
            total.append(curr)
        
        for i, num in enumerate(total[:-1]):
            if num < nums[i]:
                return False
        return True
