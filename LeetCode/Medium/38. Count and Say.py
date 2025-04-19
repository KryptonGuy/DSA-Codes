# Recursive

class Solution:
    def countAndSay(self, n: int) -> str:
        if n ==1:
            return '1'
        
        u = ''

        sq = self.countAndSay(n-1)

        i = 0

        while i < len(sq):
            j = i
            num = 0
            while j < len(sq) and sq[i] == sq[j]:
                num +=1
                j += 1
            u += str(num)
            u += str(sq[i])
            i = j

        return u

# Iterative

class Solution:
    def countAndSay(self, n: int) -> str:
        k,u = 1, '1'

        def helper(num):
            u,i = '', 0
            while i < len(num):
                cnt,j = 0,i
                while j < len(num) and num[i]==num[j]:
                    cnt+=1
                    j += 1
                u += str(cnt)
                u += str(num[i])
                i = j
            return u


        while k < n:
            u = helper(u)
            k += 1
        return u
        
        
            

        
        