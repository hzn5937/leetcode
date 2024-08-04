from collections import deque

# Define the structure for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_height(root):
    if not root:
        return 0
    
    queue = deque([root])
    height = 0
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1
    
    return height

# Example usage
# Construct a binary tree:
#       1
#      / \
#     2   3
#    / \   
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Height of the binary tree is:", binary_tree_height(root))
