class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        q=deque()
        numGoodOranges=0
        def valid(i,j):
            return 0<=i<n and 0<=j<m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    numGoodOranges+=1
        lvl=0
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if valid(i+x,j+y) and grid[i+x][j+y]==1:
                        grid[i+x][j+y]=2
                        numGoodOranges-=1
                        q.append((i+x,j+y))
            if q:
                lvl+=1
        if numGoodOranges==0:
            return lvl
        return -1