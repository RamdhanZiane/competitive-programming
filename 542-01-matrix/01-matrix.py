class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q=deque()
        n,m=len(mat),len(mat[0])
        numFlooded=0
        def valid(i,j):
            return 0<=i<n and 0<=j<m
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j))
                    numFlooded+=1
        lvl=1
        ans=[[0]*m for _ in range(n)]
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if valid(i+x,j+y) and mat[i+x][j+y]==1:
                        numFlooded+=1
                        mat[i+x][j+y]=0
                        ans[i+x][j+y]=lvl
                        q.append((i+x,j+y))
            lvl+=1
        return ans