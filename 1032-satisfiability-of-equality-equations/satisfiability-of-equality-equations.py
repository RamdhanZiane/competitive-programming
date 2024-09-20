class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        rank=defaultdict(int)
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            p1,p2 = find(x),find(y)
            if p1!=p2:
                if rank[p1]<rank[p2]:
                    parent[p1]=p2
                elif rank[p1]>rank[p2]:
                    parent[p2]=p1
                else:
                    parent[p1]=p2
                    rank[p2]+=1
        
        for a,s,_,b in equations:
            if s=='=':
                union(a,b)

        for a,s,_,b in equations:
            if s=='!' and find(a)==find(b):
                return False
        return True