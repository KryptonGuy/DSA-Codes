# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # traverse first list
        table = dict()
        currentA = headA
        while currentA:
            table[id(currentA)] = True
            currentA = currentA.next
        
        currentB = headB
        
        while currentB:
            
            if table.get(id(currentB)):
                return currentB
            
            currentB = currentB.next
        
        
            
        return None
        
        