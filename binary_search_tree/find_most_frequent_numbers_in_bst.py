from collections import Counter

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solution(root):
    array = []
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        array.append(root.val)
        inorder(root.right)
    inorder(root)
    freq = Counter(array)
    maxFreq = max(freq.values())
    return [x for x in freq if freq[x] == maxFreq]
