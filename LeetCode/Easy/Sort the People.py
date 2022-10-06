# Runtime: 167 ms, faster than 77.77% of Python3 online submissions for Sort the People.
# Memory Usage: 14.4 MB, less than 89.74% of Python3 online submissions for Sort the People.

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        table = {height:name for (height,name) in zip(heights, names)}
        heights.sort(reverse=True)
        return [table[name] for name in heights]
        
        