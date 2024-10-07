from convertTree import listToTreeNode
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.ans = None
        self.search(root, val)
        return self.ans
    
    def search(self, root, val):
        if root is None:
            return

        if root.val == val:
            self.ans = root
            return
        if root.left:
            self.search(root.left, val)
        if root.right:
            self.search(root.right, val)

root = listToTreeNode([4,2,7,1,3])
print(Solution().searchBST(root, 2).val)