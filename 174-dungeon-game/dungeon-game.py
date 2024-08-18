class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m=len(dungeon),len(dungeon[0])
        dp=[[float('inf') for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    dp[i][j]=max(-dungeon[i][j]+1,1)
                else:
                    dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        print(dp)
        return dp[0][0]