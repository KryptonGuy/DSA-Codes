class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        colm = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    colm.add(j)

        
        for num in rows:
            for j in range(len(matrix[0])):
                matrix[num][j] = 0

        for num in colm:
            for i in range(len(matrix)):
                matrix[i][num] = 0