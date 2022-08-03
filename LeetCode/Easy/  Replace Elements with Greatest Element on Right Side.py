class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxm = self.getMax(arr)
        
        for i in range(len(arr)):
            if arr[i] != maxm:
                arr[i] = maxm
                continue
            elif i == len(arr) -1:
                arr[-1] = -1
                break
            else:
                maxm = self.getMax(arr[i+1:])
                arr[i] = maxm        
        
        return arr
                    
    def getMax(self, arr):
        max1 = arr[0]
        for item in arr:
            max1 = max(max1,item)
            
        return max1

## Could also be sloved by iterating from behind and then getting the running max
    
            