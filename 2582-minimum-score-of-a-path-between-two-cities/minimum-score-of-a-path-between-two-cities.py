class unionClass:
    def __init__(self,n):
        self.parent={i:i for i in range(n)}
        self.rank=[0]*n
        self.dist=[float('inf')]*n

    def find(self,x):
        if self.parent[x]==x:
            return x
        p = self.find(self.parent[x])
        self.parent[x]=p
        return self.parent[x]

    def union(self, x,y,d):
        p1,p2=self.find(x),self.find(y)
        if p1!=p2:
            if self.rank[p1]<self.rank[p2]:
                p1,p2=p2,p1
            if self.rank[p1]==self.rank[p2]:
                self.rank[p1]+=1
            self.parent[p2]=p1
        self.dist[p1]=min(self.dist[p1],d,self.dist[p2])


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uni=unionClass(n)
        for a,b,d in roads:
            uni.union(a-1,b-1,d)
        return uni.dist[uni.find(0)]