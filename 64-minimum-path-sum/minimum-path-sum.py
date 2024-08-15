class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        dp=[[float('inf') for j in range(m+1)] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j]=grid[i][j]
                if i!=n-1 or j!=m-1:
                    dp[i][j]+=+min(dp[i+1][j],dp[i][j+1])
        return dp[0][0]