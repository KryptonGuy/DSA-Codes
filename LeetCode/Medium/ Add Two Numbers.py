# Runtime: 73 ms, faster than 90.18% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 13.9 MB, less than 86.14% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sumval = (l1.val + l2.val)
        val= sumval%10
        carry = sumval//10
        
        l1 = l1.next
        l2 = l2.next
        
        new = ListNode(val)
        dummyhead = ListNode(next=new)
        while l1 or l2:
            if not l1:
                sumval = l2.val + carry
                val= sumval%10
                carry = sumval//10
                new.next = ListNode(val)
                l2 = l2.next
            elif not l2:
                sumval = l1.val + carry
                val= sumval%10
                carry = sumval//10
                new.next = ListNode(val)
                l1 = l1.next
            else:
                sumval = l1.val + l2.val + carry
                val= sumval%10
                carry = sumval//10
                new.next = ListNode(val)
                l1 = l1.next
                l2 = l2.next
            new = new.next

        if carry!=0:
            new.next = ListNode(carry)
                
        return dummyhead.next