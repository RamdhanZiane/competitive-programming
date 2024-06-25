# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([(0,root)])
        ans=[]
        lvl_vals=[]
        prev=None
        while q:
            lvl,cur = q.popleft()
            if lvl!=prev:
                if lvl_vals:
                    ans.append(lvl_vals)
                lvl_vals=[cur.val]
                prev=lvl
            else:
                lvl_vals.append(cur.val)
            if cur.left:
                q.append((lvl+1,cur.left))
            if cur.right:
                q.append((lvl+1,cur.right))
        ans.append(lvl_vals)
        return ans