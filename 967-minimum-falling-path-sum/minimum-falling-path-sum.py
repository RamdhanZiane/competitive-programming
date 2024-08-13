from copy import deepcopy
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        dp=deepcopy(matrix)

        # def solve(i,j):
        #     if i==n or j==-1 or j==m:
        #         return 0
        #     if (i,j)
        for i in range(n-2,-1,-1):
            for j in range(m):
                dp[i][j]+=min([dp[i+1][j+y] if 0<=j+y<m else float('inf') for y in range(-1,2)])
        return min(dp[0])