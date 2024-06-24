class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        def valid(row,col):
            return 0<=row<n and 0<=col<m
        island=set()
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                        x,y=dir
                        if not valid(i+x,j+y) or not grid[i+x][j+y]:
                            ans+=1
        return ans