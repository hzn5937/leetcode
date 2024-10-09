# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        result = temp
        carry = 0

        while l1 or l2:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0
            val = d1 + d2 + carry

            if val >= 10:
                val -= 10
                carry = 1

            temp.next = ListNode(val)
            temp = temp.next

            l1 = l1.next if l1.next else None
            l2 = l2.next if l2.next else None

        if carry == 1:
            temp.next = ListNode(1)

        return result.next
