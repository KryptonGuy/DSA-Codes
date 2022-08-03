class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        table = dict()
        
        if arr.count(0) > 1:
            return True
        for item in arr:
            mul = 2 * item
            if mul == 0:
                continue
            table[mul] = item
            
        for item in arr:
            if item in table:
                return True
        
        return False