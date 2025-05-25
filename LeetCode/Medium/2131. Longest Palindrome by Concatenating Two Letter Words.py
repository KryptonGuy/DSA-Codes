class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0

        count = Counter(words)

        for key,value in count.items():
            if key[0]==key[1]:
                if value > 1:
                    ans += 4 * (value//2)
                    count[key] = value % 2

        keys = count.keys()

        for key in keys:
            if key[0]==key[1]:
                continue
            pal = ''.join([key[1],key[0]])

            if pal in count:
                ans += 4*min(count[key], count[pal])
                count[key] = 0
                count[pal] = 0

        for key,value in count.items():
            if key[0]==key[1]:
                if value> 0:
                    ans += 2
                    break
        return ans
        