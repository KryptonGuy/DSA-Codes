class Solution:
    def __init__(self):
        self.max = 0
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 0

        def cal(i, j, arr, s):

            curr = 2
            currsum = i + j

            while currsum <= arr[-1]:
                if currsum in s:
                    temp = currsum
                    currsum += j
                    j = temp
                    curr += 1
                else:
                    break
            
            self.max = max(self.max, curr)
        

        for i in range(len(arr)):
            ma = 0
            j = i + 1

            while j < len(arr):
                if arr[i] + arr[j] in s:
                    cal(arr[i], arr[j], arr, s)
                j += 1

        return self.max
        
        
                    

        