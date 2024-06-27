# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q=deque([root.left,root.right])
        while q:
            s=[]
            print(len(q))
            # if len(q)%2==1:
            #     return False
            sz=len(q)//2
            for _ in range(sz):
                cur=q.popleft()
                s.append(cur)
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
            for _ in range(sz):
                cur=q.popleft()
                pr=s.pop()
                if pr and cur:
                    if cur.val!=pr.val:
                        return False
                elif pr or cur:
                    return False
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
        return True