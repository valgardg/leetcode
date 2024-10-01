# Definition for a binary tree node.
from typing import Optional
from convertTree import listToTreeNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0

        self.traverse(root)

        return cnt

    def traverse(self, root):
        print(root.val)
        if not root.left and not root.right:
            return None
        if root.left:
            self.traverse(root.left)
        if root.right:
            self.traverse(root.right)

troot = listToTreeNode([10,5,-3,3,2,None,11,3,-2,None,1])
print(Solution().pathSum(troot, 8))