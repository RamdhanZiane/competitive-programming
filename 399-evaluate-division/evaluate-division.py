class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacency=defaultdict(set)
        visited=set()
        ops={}
        for (a,b),val in zip(equations,values):
            adjacency[a].add(b)
            adjacency[b].add(a)
            ops[(a,b)]=val
            ops[(b,a)]=1/val
        def dfs(src,dest):
            visited.add(src)
            if dest in adjacency[src]:
                return ops[(src,dest)]
            for node in adjacency[src]:
                if node not in visited:
                    res=dfs(node,dest)
                    if res:
                        return ops[(src,node)]*res
            return None

        ans=[]
        for num,denum in queries:
            visited=set()
            res = dfs(num,denum)
            if res is None:
                ans.append(-1.0)
            else:
                ans.append(res)
        return ans