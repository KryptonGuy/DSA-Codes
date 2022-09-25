# Runtime: 271 ms, faster than 83.69% of Python3 online submissions for Count Items Matching a Rule.
# Memory Usage: 20.3 MB, less than 35.41% of Python3 online submissions for Count Items Matching a Rule.

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        if ruleKey=="type":i = 0
        elif ruleKey =="color":i = 1
        else:i=2
        num, j = 0,0
        while j < len(items):
            if items[j][i]==ruleValue:num +=1   
            j += 1
        return num