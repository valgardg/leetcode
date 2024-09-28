from convertTree import listToTreeNode

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.traversedNodes = []
        self.findAncestor(root, p, q)
        # print(self.traversedNodes)
        return self.ans
    
    def findAncestor(self, root, p, q):
        add_upp = False
        # print(f'traversing node {root.val}')
        # print(f'p: {p}\nq: {q}')
        # print(f'root: {root}')
        if root == p or root == q:
            print(f'found val {root.val}')
            if root.val in self.traversedNodes and self.ans == None:
                self.ans = root
                return True
            self.traversedNodes.append(root.val)
            add_upp = True

        if root.left:
            add = self.findAncestor(root.left, p, q)
            if add:
                if root.val in self.traversedNodes and self.ans == None:
                    self.ans = root
                    return True
                self.traversedNodes.append(root.val)
                add_upp = True
        
        if root.right:
            add = self.findAncestor(root.right, p, q)
            if add:
                if root.val in self.traversedNodes and self.ans == None:
                    self.ans = root
                    return True
                self.traversedNodes.append(root.val)
                add_upp = True

        return add_upp



troot = listToTreeNode([3,5,1,6,2,0,8,None,None,7,4])
# wrong representation of P and Q
print(Solution().lowestCommonAncestor(troot, listToTreeNode([5,1,6,2,0,8,None,None,7,4]),listToTreeNode([1,6,2,0,8,None,None,7,4])))


# troot2 = listToTreeNode([3,5,1,6,2,0,8,None,None,7,4])
# print(Solution().lowestCommonAncestor(troot2, listToTreeNode([5]),listToTreeNode([4])))