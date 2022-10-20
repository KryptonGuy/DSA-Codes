# Runtime: 57 ms, faster than 77.61% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 14 MB, less than 29.79% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = dummy = ListNode(-1000, head)
        while head:
            if pre.val == head.val:
                pre.next = head.next
                head = head.next
                continue
            pre = head
            head = head.next
        return dummy.next
            
                
        