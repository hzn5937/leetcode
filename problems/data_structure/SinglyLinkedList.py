class Node:
    
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right

    def get(self, index: int) -> int:
        cur = self.left.next
        while (cur and index > 0):
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.left.next
        self.left.next = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        cur = self.left
        while (cur.next != self.right):
            cur = cur.next
        node.next = cur.next
        cur.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        cur = self.left
        while (cur.next != self.right and index > 0):
            cur = cur.next
            index -= 1
        if index == 0:
            node.next = cur.next
            cur.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left
        while (cur.next.next != self.right and index > 0):
            cur = cur.next
            index -= 1
        if index == 0:
            cur.next = cur.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)