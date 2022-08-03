class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        size = len(arr)
        i = 1
        up = False
        down = False
        # Go Up
        
        while i < size and arr[i] > arr[i-1]:
            i += 1
            up = True
        
        # Go Down
        
        while i < size and arr[i] < arr[i-1]:
            i += 1
            down = True
            
        if up and down and i==size:
            return True