import math
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.ans = math.inf
        def solve(cookie, dist):
            if max(dist)>=self.ans:
                return
            if cookie==len(cookies):
                self.ans = min(self.ans, max(dist))
                return
            for i in range(k):
                dist[i]+=cookies[cookie]
                solve(cookie+1,dist)
                dist[i]-=cookies[cookie]
        solve(0,[0]*k)
        return self.ans