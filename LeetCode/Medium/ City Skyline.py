# Runtime: 78 ms, faster than 95.42% of Python3 online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 13.8 MB, less than 99.73% of Python3 online submissions for Max Increase to Keep City Skyline.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row, col = dict(), dict()
        ans, n = 0 , len(grid)
        for i in range(n):
            row[i] = max(grid[i])
            m = 0
            for j in range(n):
                m = max(m, grid[j][i])
            col[i] = m
        
        i , j = 0, 0
        while j < n:
            i = 0
            while i < n:
                h = (min(row[i], col[j]) - grid[i][j])
                if h >0:   
                    ans += h 
                i += 1
            j+= 1
            
        
        return ans
        
        