# Runtime: 66 ms, faster than 38.13% of Python3 online submissions for Maximum Number of Balloons.
# Memory Usage: 13.8 MB, less than 99.55% of Python3 online submissions for Maximum Number of Balloons.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter, count, ball = collections.Counter(text), 0, {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}

        while True:
            for bal in ball.keys():
                if counter[bal] - ball[bal] <0:
                    return count
                counter[bal] = counter[bal] - ball[bal]
            count += 1            