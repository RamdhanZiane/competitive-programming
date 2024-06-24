import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        adjacency=defaultdict(set)
        for k,(x,y,r) in enumerate(bombs):
            for kk,(i,j,_) in enumerate(bombs):
                if kk!=k and math.sqrt((i-x)**2+(j-y)**2)<=r:
                    adjacency[k].add(kk)

        ans=1
        detonated=None

        def detonate(bomb):
            res=1
            for b in adjacency[bomb]:
                if b not in detonated:
                    detonated.add(b)
                    res+=detonate(b)
            return res

        for bomb in range(n):
            detonated={bomb}
            ans=max(ans,detonate(bomb))
        return ans