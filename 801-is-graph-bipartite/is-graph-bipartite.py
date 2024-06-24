class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        stk=[0]
        colors={0:0}
        visited=set()
        for n in range(len(graph)):
            if n not in visited:
                stk.append(n)
                colors[n]=0
            while stk:
                cur=stk.pop()
                visited.add(cur)
                for node in graph[cur]:
                    if node not in visited:
                        colors[node]=1-colors[cur]
                        stk.append(node)
        for node in range(len(graph)):
            for neigh in graph[node]:
                if colors[neigh]==colors[node]:
                    return False
        return True