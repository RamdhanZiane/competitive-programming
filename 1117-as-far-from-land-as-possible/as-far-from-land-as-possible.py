class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q=deque()
        n,m=len(grid),len(grid[0])
        numFlooded=n*m
        def valid(i,j):
            return 0<=i<n and 0<=j<m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j))
                    numFlooded-=1
        if numFlooded==0 or numFlooded==n*m:
            return -1
        lvl=1
        while q:
            print(q)
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if valid(i+x,j+y) and grid[i+x][j+y]==0:
                        numFlooded-=1
                        grid[i+x][j+y]=1
                        q.append((i+x,j+y))
                        if numFlooded==0:
                            return lvl
            lvl+=1