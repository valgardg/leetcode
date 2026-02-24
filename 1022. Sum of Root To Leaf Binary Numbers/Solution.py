# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        paths = []
        
        def enterNode(node, path):
            path += str(node.val)

            if node.left:
                enterNode(node.left, path)
            if node.right:
                enterNode(node.right, path)

            if node.left == None and node.right == None:
                paths.append(path)

        print(paths)
            
        return sum([int(path, 2) for path in paths])
    
print(Solution().sumRootToLeaf(TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1)))))
