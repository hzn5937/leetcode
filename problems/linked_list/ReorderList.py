from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    queue = deque()
    count = 0

    cur = head
    while cur:
        if count % 2:
            queue.append(cur)
        #     1,2,3,4 [1]
        else:
            queue.appendleft(cur)
        count += 1
        cur = cur.next

    cur = queue.popleft()
    while queue:
        cur.next = queue.popleft()



