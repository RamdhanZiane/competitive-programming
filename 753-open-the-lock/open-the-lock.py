from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set([tuple(map(int,list(d))) for d in deadends])
        lvl=0
        q=deque([[0,0,0,0]])
        t=list(map(int,list(target)))
        visited=set()
        while q:
            sz=len(q)
            for _ in range(sz):
                cur=q.popleft()
                if cur==t:
                    return lvl
                curr=tuple(cur)
                if curr not in dead and curr not in visited:
                    for i in range(4):
                        cur[i] = (cur[i]+1)%10
                        q.append(cur.copy())
                        cur[i] = (cur[i]-2)%10
                        q.append(cur.copy())
                        cur[i] = (cur[i]+1)%10
                visited.add(curr)
            lvl+=1
        return -1