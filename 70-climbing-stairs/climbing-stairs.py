memo={1:1,2:2}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n not in memo:
            memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return memo[n]