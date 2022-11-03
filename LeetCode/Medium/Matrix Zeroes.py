# Runtime: 145 ms, faster than 84.29% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.7 MB, less than 90.73% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i, j = 0 , 0
        row, col = dict(), dict()
        
        while j < len(matrix):
            i =0
            while i < len(matrix[0]):
                if matrix[j][i]==0:
                    row[i] = True
                    col[j] = True
                i += 1
            j += 1
        for ro in row.keys():
            j= 0
            while j < len(matrix):
                matrix[j][ro] = 0
                j += 1
                
        for co in col.keys():
            i = 0
            while i < len(matrix[0]):
                matrix[co][i] = 0
                i += 1
