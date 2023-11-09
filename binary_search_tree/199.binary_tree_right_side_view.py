from collections import deque
def rightSideView(root):
    res = []
    queue = deque()
    if root:
        queue.append(root)
    while len(queue) > 0:
        temp = []
        for i in range(len(queue)):
            curr = queue.popleft()
            temp.append(curr.val)                
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(temp[-1])
    return res