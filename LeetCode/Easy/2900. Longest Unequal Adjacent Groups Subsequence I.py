class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:

        i = 1
        ans = [words[0]]
        last = groups[0]
        while i < len(words):
            if groups[i]!= last:
                ans.append(words[i])
                last = groups[i]
            i +=1
        return ans



        