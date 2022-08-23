# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
#         if head.next:
#             self.isPaindrome(head)
        
#         ans
#         return self.first == head

        some = []
    
        while head:
            some.append(head.val)
            head = head.next

        i = 0
        j = len(some) - 1
    
        return some == some[::-1]
        