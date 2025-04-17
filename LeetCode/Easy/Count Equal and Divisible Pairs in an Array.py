class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        i,ans = 0,0

        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i]==nums[j] and ((i*j)%k)==0:
                    ans += 1

                j +=1
            i +=1
        return ans
        