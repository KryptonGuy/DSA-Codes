# Runtime: 237 ms, faster than 66.16% of Python3 online submissions for Merge Intervals.
#Memory Usage: 18.1 MB, less than 85.06% of Python3 online submissions for Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i+1][1] > intervals[i][1]:
                    s = intervals[i+1][1]
                else:
                    s = intervals[i][1]
                intervals.insert(i, [intervals[i][0],s])
                intervals.pop(i+1)
                intervals.pop(i+1)
                continue

            i += 1
        
        return intervals
            