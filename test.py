class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        
        while (cur):
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp
        
        return prev