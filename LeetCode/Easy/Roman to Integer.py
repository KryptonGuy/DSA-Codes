class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        i = ans = 0
        
        while i < len(s):
            
            try:
                if s[i] =="I" and (s[i+1]=="V" or s[i+1]=="X"):
                    ans += table[s[i+1]] - table[s[i]]
                    i += 2
                elif s[i] =="X" and (s[i+1]=="L" or s[i+1]=="C"):
                    ans += table[s[i+1]] - table[s[i]]
                    i += 2
                elif s[i] =="C" and (s[i+1]=="D" or s[i+1]=="M"):
                    ans += table[s[i+1]] - table[s[i]]
                    i += 2
                else:
                    ans += table[s[i]]
                    i +=1
            except:
                ans += table[s[i]]
                i += 1
            
        return ans
                    
                    
            