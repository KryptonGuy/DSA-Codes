# Runtime: 54 ms, faster than 55.91% of Python3 online submissions for Count Sorted Vowel Strings.
# Memory Usage: 13.8 MB, less than 67.19% of Python3 online submissions for Count Sorted Vowel Strings.

class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(n-1):
            for j in range(4, -1,-1):
                dp[j] += sum(dp[:j])       
        return sum(dp)