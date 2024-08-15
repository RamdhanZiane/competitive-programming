class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}

        def solve(c,l):
            if l==len(t):
                return 1
            if c==len(s):
                return 0
            if (c,l) not in memo:
                include=0
                if s[c]==t[l]:
                    include=solve(c+1,l+1)
                memo[(c,l)] = solve(c+1,l)+include
            return memo[(c,l)]
        return solve(0,0)