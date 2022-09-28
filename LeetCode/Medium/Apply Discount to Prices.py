# Runtime: 238 ms, faster than 52.22% of Python3 online submissions for Apply Discount to Prices.
# Memory Usage: 16 MB, less than 88.89% of Python3 online submissions for Apply Discount to Prices.

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        split = sentence.split()
        for i, word in enumerate(split):
            if word[0]=="$"and word[1:].isdigit():
                num = int(word[1:])*(1-(discount/100))
                
                inter = "${:.2f}".format(num)
                
                split[i] = inter
        
        return ' '.join(split)