class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q=deque()
        n,m=len(isWater),len(isWater[0])
        ans=[[0]*m for _ in range(n)]
        def valid(i,j):
            return 0<=i<n and 0<=j<m
        for i in range(n):
            for j in range(m):
                if isWater[i][j]==1:
                    q.append((i,j))
        lvl=1
        while q:
            print(q)
            for _ in range(len(q)):
                i,j=q.popleft()
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    if valid(i+x,j+y) and isWater[i+x][j+y]==0:
                        isWater[i+x][j+y]=1
                        q.append((i+x,j+y))
                        ans[i+x][j+y]=lvl
            lvl+=1
        return ans