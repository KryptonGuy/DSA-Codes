# Runtime: 144 ms, faster than 91.09% of Python3 online submissions for Missing Number.
# Memory Usage: 15.6 MB, less than 11.91% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        table = {x:False for x in range(len(nums))}
        for num in nums:
            table[num] = True
        for key in table.keys():
            if not table[key]:
                return key
        return len(nums)