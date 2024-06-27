class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        radjacency,badjacency=defaultdict(list),defaultdict(list)
        for u,v in redEdges:
            radjacency[u].append(v)
        for u,v in blueEdges:
            badjacency[u].append(v)
        ans=[-1]*n
        
        def bfs(prev):
            q=deque([0])
            lvl=0
            rvisited,bvisited=set(),set()
            if prev:
                bvisited.add(0)
            else:
                rvisited.add(0)
            while q:
                for _ in range(len(q)):
                    cur=q.popleft()
                    if ans[cur]==-1:
                        ans[cur]=lvl
                    else:
                        ans[cur]=min(ans[cur],lvl)
                    if prev==0:
                        for neigh in badjacency[cur]:
                            if neigh not in bvisited:
                                q.append(neigh)
                                bvisited.add(neigh)
                    else:
                        for neigh in radjacency[cur]:
                            if neigh not in rvisited:
                                q.append(neigh)
                                rvisited.add(neigh)
                lvl+=1
                prev=1-prev
        bfs(0)
        bfs(1)
        return ans