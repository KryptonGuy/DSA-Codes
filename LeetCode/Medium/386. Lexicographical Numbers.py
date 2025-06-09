
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        def helper(num):
            ans.append(num)

            for i in range(0,10):
                temp = num*10 + i
                if temp <= n:
                    helper(temp)
                else:
                    break
            return

        for i in range(1,10):
            if i <= n:
                helper(i)
        return ans

        


