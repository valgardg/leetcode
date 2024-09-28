from convertTree import listToTreeNode
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxcnt = 0
        if root.right:
            self.zigzag(root.right, 1, 'r')
        if root.left:
            self.zigzag(root.left, 1, 'l')
        return self.maxcnt

    def zigzag(self, root, count, ddir='r'):
        # print('right' if ddir == 'r' else 'left')
        # print(f'count: {count}')
        if count > self.maxcnt:
            self.maxcnt = count
        if not root.left and not root.right:
            return
        if ddir == 'l':
            if root.right:
                count = count + 1
                self.zigzag(root.right, count, 'r')
            if root.left:
                count = 1
                self.zigzag(root.left, count, 'l')
        else:
            if root.left:
                count = count + 1
                self.zigzag(root.left, count, 'l')
            if root.right:
                count = 1
                self.zigzag(root.right, count, 'r')
        
        return


root = listToTreeNode([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
print(Solution().longestZigZag(root))
root = listToTreeNode([1,1,1,None,1,None,None,1,1,None,1])
print(Solution().longestZigZag(root))