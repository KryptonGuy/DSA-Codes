class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rang = {i for i in range(1,len(nums) +1)}
        return rang-set(nums)
