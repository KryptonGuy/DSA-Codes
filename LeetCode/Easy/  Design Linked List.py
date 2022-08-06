class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = 0
        node = self.head
        
        while node:
            if index==curr:
                return node.val
            curr += 1
            node = node.next
            
        return -1
            
            

    def addAtHead(self, val: int) -> None:
        if self.head:
            newHead = Node(val, self.head)
            self.head = newHead
        else:
            self.head = Node(val)
            

    def addAtTail(self, val: int) -> None:
        
        node = self.head
        if not node:
            self.addAtHead(val)
        while node:
            if not node.next:
                node.next = Node(val)
                return
            node = node.next
            

    def addAtIndex(self, index: int, val: int) -> None:
        curr = 0
        node = self.head
        pre = None
        
        if index == 0:
            self.addAtHead(val)
            return
        
        while node:
            if curr==index:
                new = Node(val, node)
                pre.next = new
                return
            pre = node
            node = node.next
            curr += 1
            
        if curr == index:
            self.addAtTail(val)
        

    def deleteAtIndex(self, index: int) -> None:
        curr = 0
        node = self.head
        pre = None
        
        if index == 0:
            self.head = self.head.next
            return
        
        while node:
            if curr==index:
                pre.next = node.next
                del node
                return
            pre = node
            node = node.next
            curr += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)