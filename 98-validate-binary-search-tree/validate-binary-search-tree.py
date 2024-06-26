import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = -math.inf
        inOrder = []
        s = []
        while True:
            if root:
                s.append(root)
                root = root.left
            else:
                if not s:
                    break
                root = s[-1]
                if root.val <= prev:
                    return False
                prev = root.val
                s.pop()
                root = root.right
        return True