class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        n,m=len(grid),len(grid[0])

        def verify(i,j):
            return 0<=i<n and 0<=j<m
        def dfs(i,j):
            visited.add((i,j))
            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                if verify(i+x,j+y) and grid[i+x][j+y]=='1' and not (i+x,j+y) in visited:
                    dfs(i+x,j+y)

        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and not (i,j) in visited:
                    dfs(i,j)
                    ans+=1
        return ans