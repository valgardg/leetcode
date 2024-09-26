# Definition for a binary tree node.
from typing import Optional
from convertTree import listToTreeNode

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ll = self.searchLeaves(root1)
        rl = self.searchLeaves(root2)
        print(f'left leaves: {ll}')
        print(f'left leaves: {rl}')
        return ll == rl
    
    def searchLeaves(self, root):
        leaves = []
        if root.left:
            leaves.extend(self.searchLeaves(root.left))
        if root.right:
            leaves.extend(self.searchLeaves(root.right))
        # if no right and left, we are a leaf
        if not (root.left) and not (root.right):
            return [root.val]
        return leaves


root1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]

tree1 = listToTreeNode(root1)
tree2 = listToTreeNode(root2)

print(Solution().leafSimilar(tree1, tree2))