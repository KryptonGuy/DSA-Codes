# Runtime: 46 ms, faster than 64.85% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.
# Memory Usage: 13.8 MB, less than 57.18% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.

class Solution:
    def minimumSum(self, num: int) -> int:
        strr, listt = str(num), []
        for nu in strr:
            listt.append(int(nu))
        listt.sort()
        return sum(listt[:2])*10 + sum(listt[2:])
             