import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(lambda: [math.inf,-math.inf])
        def solve(node,lvl,num):
            if not node:
                return
            levels[lvl][0] = min(levels[lvl][0],num)
            levels[lvl][1] = max(levels[lvl][1],num)
            rnum = 2*num
            lnum = rnum-1
            solve(node.left,lvl+1,lnum)
            solve(node.right,lvl+1,rnum)
        solve(root,0,1)
        ans = 0
        for key, (l,r) in levels.items():
            ans = max(ans,r-l+1)
        return ans