# Runtime: 63 ms, faster than 48.31% of Python3 online submissions for Beautiful Array.
# Memory Usage: 14.2 MB, less than 25.12% of Python3 online submissions for Beautiful Array.

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        arr = list(range(1,n+1))
        
        def helper(arr):
            if len(arr) <3:
                return arr
            odd, even = arr[1::2], arr[::2]
            return helper(odd) + helper(even)
        return helper(arr)
         