class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def solve(start, end):
            chars = set(s[start:end])
            for c in range(start,end):
                if s[c].upper() not in chars or s[c].lower() not in chars:
                    a1,b1 = solve(start,c)
                    a2,b2 = solve(c+1,end)
                    if b1-a1 >= b2-a2:
                        return a1,b1
                    return a2,b2
            return start,end
        a,b = solve(0,len(s))
        return s[a:b]