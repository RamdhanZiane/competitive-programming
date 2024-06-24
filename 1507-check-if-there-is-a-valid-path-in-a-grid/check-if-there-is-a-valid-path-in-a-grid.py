class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n,m=len(grid),len(grid[0])
        directing={
            1:[(0,-1),(0,1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(1,0),(0,1)],
            5:[(-1,0),(0,-1)],
            6:[(-1,0),(0,1)]
        }
        coming={
            (0,1):[1,3,5],
            (0,-1):[1,4,6],
            (1,0):[2,5,6],
            (-1,0):[2,3,4]
        }
        
        def valid(i,j):
            return 0<=i<n and 0<=j<m

        visited=set()
        def dfs(i,j):
            if i==n-1 and j==m-1:
                return True
            visited.add((i,j))
            for x,y in directing[grid[i][j]]:
                if valid(i+x,j+y) and not (i+x,j+y) in visited and grid[i+x][j+y] in coming[(x,y)]:
                    if dfs(i+x,j+y):
                        return True
            return False
        
        return dfs(0,0)
