class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        n=len(questions)
        dp=[0]*(n+1)
        for q in range(n-1,-1,-1):
            dp[q] = max(questions[q][0]+dp[min(n,q+questions[q][1]+1)], dp[q+1])
        return dp[0]