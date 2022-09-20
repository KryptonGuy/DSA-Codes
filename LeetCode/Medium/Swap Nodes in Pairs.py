# Runtime: 40 ms, faster than 76.88% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13.8 MB, less than 64.32% of Python3 online submissions for Swap Nodes in Pairs.
# Next challenges


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        if not head:
            return None
        
        if not head.next:
            return head
        
        if head.next.next:
            pre = self.swapPairs(head.next.next)

        if head.next:
            temp = head.next
            head.next = pre
            temp.next = head
            return temp
        
        return None
            
        