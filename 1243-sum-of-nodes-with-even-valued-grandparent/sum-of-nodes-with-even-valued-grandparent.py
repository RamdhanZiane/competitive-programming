# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        def solve(root,parent,gparent):
            if not root:
                return 0
            v=0
            if gparent:
                v=root.val
            print(root.val,parent,gparent)
            return v+solve(root.right,root.val%2==0,parent)+solve(root.left,root.val%2==0,parent)
        return solve(root,False,False)