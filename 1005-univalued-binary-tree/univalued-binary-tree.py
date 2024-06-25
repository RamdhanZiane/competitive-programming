from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        v = root.val
        q=deque([root])
        while q:
            cur = q.popleft()
            if cur.val!=v:
                return False
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return True