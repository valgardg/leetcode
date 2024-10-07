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
        if root.val == key:
            return None
        def searchBST(root, parent):
            if not root:
                return
            print(f'looking at node: {root.val}')
            if root.val > key:
                return searchBST(root.left, root)
            if root.val < key:
                return searchBST(root.right, root)
            # here we knwo t
            lnode = root.left
            rnode = root.right
            if root.val > parent.val:
                parent.right = rnode
                rnodeleft = rnode
                while rnodeleft.left:
                    rnodeleft = rnodeleft.left
                rnodeleft.left = lnode
            if root.val < parent.val:
                parent.left = rnode
                rnodeleft = rnode
                while rnodeleft.left:
                    rnodeleft = rnodeleft.left
                rnodeleft.left = lnode
            parent.left = None
            parent.right = None

        searchBST(root, root)

        return root

# root = listToTreeNode([5,3,6,2,4,None,3])
# print(Solution().deleteNode(root, 3))
root = listToTreeNode([0])
print(Solution().deleteNode(root, 0).val)