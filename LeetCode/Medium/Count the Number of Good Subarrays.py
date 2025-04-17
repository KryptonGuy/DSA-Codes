class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0

        curr,j = 0, -1
        has = Counter()

        for i in range(len(nums)):
            while curr < k and j + 1 < len(nums):
                j += 1
                curr += has[nums[j]]
                has[nums[j]] += 1
            
            if curr >=k:
                ans += len(nums) - j
            has[nums[i]] -= 1
            curr -= has[nums[i]]
        
        return ans