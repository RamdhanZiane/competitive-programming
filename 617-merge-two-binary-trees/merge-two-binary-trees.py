# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        if root1 and root2:
            root1.val += root2.val
            root1.right = self.mergeTrees(root1.right,root2.right)
            root1.left = self.mergeTrees(root1.left, root2.left)
            return root1
        else:
            if root1:
                root1.right = self.mergeTrees(root1.right,None)
                root1.left = self.mergeTrees(root1.left, None)
                return root1
            elif root2:
                root2.right = self.mergeTrees(None, root2.right)
                root2.left = self.mergeTrees(None, root2.left)
                return root2
            return None