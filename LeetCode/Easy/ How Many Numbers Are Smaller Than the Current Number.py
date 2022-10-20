# Runtime: 66 ms, faster than 94.26% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14 MB, less than 47.32% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sor = sorted(nums)
        table, ans = dict(), []
        for i in range(len(sor)-1, -1,-1):
            table[sor[i]] = i
                    
        for num in nums:
            ans.append(table[num])
        print(table, sor)
        return ans
        
        
        