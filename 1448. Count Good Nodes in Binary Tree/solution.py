from convertTree import listToTreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = self.searchRoot(root, root.val)

        return cnt
    
    def searchRoot(self, root, maxval):
        # print(f'checking node {root.val}')
        cnt = 0
        if root.val >= maxval:
            # print(f'{root.val} is a good node')
            cnt += 1
        if not root.left and not root.right:
            return cnt
        
        if root.val > maxval:
            maxval = root.val

        if root.left:
            cnt += self.searchRoot(root.left, maxval)
        if root.right:
            cnt += self.searchRoot(root.right, maxval)
        return cnt

root1 = [3,1,4,3,None,1,5]

tree1 = listToTreeNode(root1)

print(Solution().goodNodes(tree1))