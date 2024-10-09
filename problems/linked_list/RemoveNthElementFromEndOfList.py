from typing import Optional
class ListNode:
    def __init__(self,val=0, next=None):
        self.next = next
        self.val = val

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        left = temp
        right = head

        # right is an offset between last element and removing element
        while n > 0:
            right = right.next
            n -= 1

        # traverse until right is Null. At this point left.next is the removing element
        while right.next:
            left = left.next
        left.next = left.next.next
        return temp.next
