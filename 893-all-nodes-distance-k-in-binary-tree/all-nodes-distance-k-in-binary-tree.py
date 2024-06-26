# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k==0:
            return [target.val]
        
        # Search
        parents={}
        def search(node):
            if not node:
                return
            if node==target:
                return node
            if node.right:
                parents[node.right]=node
                res=search(node.right)
                if res is not None:
                    return res
            if node.left:
                parents[node.left]=node
                res=search(node.left)
                if res is not None:
                    return res
            return None
        t=search(root)
        node=t
        lvl=0
        ans=[]
        visited=set([node])
        

        def bfs(node,l):
            q=deque([node])
            while q:
                if l==k:
                    while q:
                        ans.append(q.popleft().val)
                else:
                    for _ in range(len(q)):
                        cur=q.popleft()
                        visited.add(cur)
                        if cur.left and cur.left not in visited:
                            q.append(cur.left)
                        if cur.right and cur.right not in visited:
                            q.append(cur.right)
                    l+=1
        
        while node in parents and lvl<=k:
            visited.add(node)
            bfs(node,lvl)
            node=parents[node]
            lvl+=1
        if lvl<=k:
            bfs(node,lvl)

        return ans