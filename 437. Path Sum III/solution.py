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
        count = 0
        self.paths = []
        self.traverse(root, [])
        for path in self.paths:
            if sum(path) == targetSum:
                count += 1
            if sum(path) > targetSum:
                # handle something
                lp, rp = 0, len(path)
                while :
                    
                pass
            
        return count

    def traverse(self, root, path):
        path.append(root.val)
        self.paths.append(list(path))
        if root.left:
            self.traverse(root.left, list(path))
        if root.right:
            self.traverse(root.right, list(path))
        return 

troot = listToTreeNode([10,5,-3,3,2,None,11,3,-2,None,1])
print(Solution().pathSum(troot, 8))