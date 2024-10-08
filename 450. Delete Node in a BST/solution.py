from collections import deque
from utils.treeToList import treeToList
from utils.convertToTree import listToTreeNode
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            print(f'looking at {root.val}, going into {root.right.val}')
            root.right = self.deleteNode(root.right, key)
        # found our key
        else:
            print(f'found key: {root.val}')
            # no children
            if not root.left and not root.right:
                print(f'returning none womp womp')
                return None
            # no right
            if root.left and not root.right:
                return root.left
            # no left
            if not root.left and root.right:
                return root.right
            # two children
            if root.left and root.right:
                minval = self.findmin(root.right)
                root.val = minval
                root.right = self.deleteNode(root.right, root.val)
        return root

    def findmin(self, root):
        node = root
        while node.left:
            node = node.left
        nodeval = node.val
        node = None
        return nodeval

root = listToTreeNode([5,3,6,2,4,None,7])
sol = Solution().deleteNode(root, 3)
print(treeToList(sol))

# root = listToTreeNode([5,3,6,2,4,None,7])
# sol = Solution().deleteNode(root, 7)
# print(treeToList(sol))