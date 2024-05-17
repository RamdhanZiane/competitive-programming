# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def inorder(root):
            if not root:
                return None
            a = inorder(root.left)
            if a is not None:
                return a
            self.count+=1
            if k==self.count:
                return root.val
            return inorder(root.right)
        return inorder(root)
