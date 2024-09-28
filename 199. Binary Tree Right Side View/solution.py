from typing import List, Optional
from convertTree import listToTreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        self.levels = {}
        self.searchTree(root, 0)
        return list(self.levels.values())
    
    def searchTree(self, root, depth):
        # if we are at a leaf node
        if root.left == None and root.right == None:
            if depth in self.levels:
                self.levels[depth] = root.val
            else:
                self.levels[depth] = root.val
            return
        
        if depth in self.levels:
            self.levels[depth] = root.val
        else:
            self.levels[depth] = root.val
        if root.left:
            self.searchTree(root.left, depth+1)
        if root.right:
            self.searchTree(root.right, depth+1)
        return


    
        
    
root = listToTreeNode([1,2,3,None,5,None,4])
print(Solution().rightSideView(root))