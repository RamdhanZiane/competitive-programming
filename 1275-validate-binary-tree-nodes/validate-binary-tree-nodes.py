class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        roots=set(range(n))
        for node in range(n):
            if leftChild[node] in roots:
                roots.remove(leftChild[node])
            if rightChild[node] in roots:
                roots.remove(rightChild[node])
        if len(roots)!=1:
            return False
        visited=set([next(iter(roots))])
        q=deque([next(iter(roots))])
        while q:
            cur=q.popleft()
            if leftChild[cur]!=-1:
                if leftChild[cur] in visited:
                    return False
                q.append(leftChild[cur])
                visited.add(leftChild[cur])
            if rightChild[cur]!=-1:
                if rightChild[cur] in visited:
                    return False
                q.append(rightChild[cur])
                visited.add(rightChild[cur])
        return len(visited)==n