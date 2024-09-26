# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        sq = [root] # search queue
        nq = [] # next queue
        cnt = 0
        while len(sq) > 0:
            cnt += 1
            for n in sq:
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            sq = nq
            nq = []

        return cnt
    
