from collections import defaultdict
from convertTree import listToTreeNode
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = {}
        roots = [[root, 1]]
        while len(roots) > 0:
            root_and_depth = roots.pop(0)
            root = root_and_depth[0]
            depth = root_and_depth[1]
            if depth not in levels:
                levels[depth] = 0 
            levels[depth] += root.val
            if root.left:
                roots.append([root.left, depth+1])
            if root.right:
                roots.append([root.right, depth+1])
            
        


        return max(levels, key=levels.get)
    
root = listToTreeNode([1,7,0,7,-8,None,None])
print(Solution().maxLevelSum(root))