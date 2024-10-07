from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listToTreeNode(lst):
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()

        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1

        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root