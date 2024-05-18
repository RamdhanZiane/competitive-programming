# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def solve(root):
            if not root:
                return None
            l1 = l2 = r1 = r2 = root.val
            if root.right:
                l1,r1 = solve(root.right)
            if root.left:
                l2,r2 = solve(root.left)
            l,r = min(l1,l2), max(r1,r2)
            self.res = max(self.res, abs(root.val-l), abs(root.val-r))
            l,r = min(l,root.val), max(r,root.val)
            return l,r
        solve(root)
        return self.res