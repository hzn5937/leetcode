class Node:

    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

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
        right = self.left.next
        node.next = right
        node.prev = self.left
        self.left.next = node
        right.prev = node
        

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        left = self.right.prev
        
        node.next = self.right
        node.prev = left
        
        left.next = node
        self.right.prev = node
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        cur = self.left
        while (cur.next != self.right and index > 0):
            cur = cur.next
            index -= 1
        if (index == 0):
            right = cur.next
            node.next = right
            node.prev = cur
            cur.next = node
            right.prev = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left
        while (cur.next.next != self.right and index > 0):
            cur = cur.next
            index -=1
        if index == 0:
            cur.next = cur.next.next
            cur.next.prev = cur
        