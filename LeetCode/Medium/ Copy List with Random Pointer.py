# Runtime: 37 ms, faster than 94.51% of Python3 online submissions for Copy List with Random Pointer.
# Memory Usage: 14.8 MB, less than 82.77% of Python3 online submissions for Copy List with Random Pointer.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        bed = head
        table = dict()
        dummy = newhead = Node(0)
        
        while head:
            new = Node(head.val)
            newhead.next = new
            newhead = new
            table[head]=new
            head = head.next
        while bed:
            node = table[bed]
            if bed.random:
                node.random = table[bed.random]
            else:
                node.random = None
            bed = bed.next
        
        return dummy.next
        
            
            
            
        