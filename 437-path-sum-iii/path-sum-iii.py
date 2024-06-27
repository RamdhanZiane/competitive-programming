# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums=defaultdict(int)
        sums[0]=1
        def dfs(node,sum_):
            if not node:
                return 0
            sum_+=node.val
            count=sums[sum_-targetSum]
            sums[sum_]+=1
            count+=dfs(node.left,sum_)+dfs(node.right,sum_)
            sums[sum_]-=1
            return count
        return dfs(root,0)
            