# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def bottom(node,d):
            if node:
                
                if node.right:
                    v2,d2 = bottom(node.right, d+1)
                else:
                    v2,d2 = 0, -1
                if node.left:
                    v1,d1 = bottom(node.left,d+1)
                else:
                    v1,d1 = node.val, d
                if d1>=d2:
                    return v1,d1
                return v2,d2                
            else:
                return 0, -1

        v,d = bottom(root,0)
        return v
                
            