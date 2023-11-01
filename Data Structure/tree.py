class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def get_minimum_node(root):
    cur = root
    while cur and cur.left:
        cur = cur.left
    return cur

def remove(root, value):
    if not root:
        return None
    
    if value < root.value:
        root.left = remove(root.left, value)
    elif value > root.value:
        root.right = remove(root.right, value)
    else:
        # check if node has one or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = get_minimum_node(root.right) # get minimum value of right subtree
            root.value = minNode.value # replace the value of removing node with minimum value above
            root.right = remove(root.right, minNode.value) # remove the minimum value Node
            # remove the node by replacing it with the minimum right subtree value, and remove the minimum value node
    return root

def insert(root, value):
    if not root:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if not root:
        return False
    
    if value < root.value:
        return search(root.left, value)
    elif value > root.value:
        return search(root.right, value)
    else:
        return True

# traversal
# Depth First Search (DFS)
def inorder(root):
    if not root: 
        return
    inorder(root.left)
    print(root.value, end = " ")
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.value, end = " ")  # Visit the root
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end = " ")  # Visit the root

# Breadth First Search (BFS)
def levelorder(root):
    if not root:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].value, end = " ")
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


root = Node(4)
insert(root, 3)
insert(root,2)
insert(root, 6)
insert(root,5)
insert(root, 7) 
print("inorder traversal:")
inorder(root)
print("\npreorder traversal:")
preorder(root)
print("\npostorder traversal:")
postorder(root)
print("\nlevelorder traversal:")
levelorder(root)