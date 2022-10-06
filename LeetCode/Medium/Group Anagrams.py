# Runtime: 194 ms, faster than 47.12% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.2 MB, less than 89.17% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = dict()
        
        for word in strs:
            sorte = sorted(word)
            wor = ''.join(sorte)            
            if wor in table.keys():
                table[wor].append(word)
                continue
            
            table[wor] = [word]
            
        return [i for i in table.values()]
                