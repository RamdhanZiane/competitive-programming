# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pfound = self.qfound = False
        self.found = None
        def solve(root):
            if not root:
                return False
            if root == p:
                self.pfound = True
                return True
            if root == q:
                self.qfound = True
                return True
            a = solve(root.left)
            b = solve(root.right)
            if a and b:
                self.found = root
                return True
            if a or b:
                return True
            return False
        solve(root)
        if self.found:
            return self.found
        if self.qfound:
            return q
        return p