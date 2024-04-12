class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
class Solution:
    def reverseList(self, head):
        cur = head
        prev = None
        
        # adjust pointer at prev variable and using temp to move to next Node without a link
        while (cur):
            temp = cur.next
            cur.next = prev
            prev = cur 
            cur = temp
        
        return prev