class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        size = len(arr)
        i = 0
        while i < size -1:
            if arr[i]==0:
                dup = arr[i+1:]
                arr[i+1] = 0
                for j in range(size -i -2):
                    arr [i+j+2] = dup[j]
                i += 1
            i += 1