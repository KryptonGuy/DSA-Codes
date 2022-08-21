# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        end = head
        curr = head
        
        for i in range(n):
            end= end.next
            
        if not end:
            return head.next
        
        while end.next:
            end = end.next
            curr = curr.next
        
        if n ==1:
            curr.next = None
            return head
            
        curr.next = curr.next.next

        return head