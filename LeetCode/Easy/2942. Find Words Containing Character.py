class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans,i = [],0

        while i  < len(words):
            for char in words[i]:
                if x==char:
                    ans.append(i)
                    break
            
            i += 1
        return ans