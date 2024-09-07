class unionClass:
    def __init__(self,stones):
        self.parent={}
        self.rank=defaultdict(int)

    def find(self,x):
        if not x in self.parent:
            self.parent[x]=x
        if self.parent[x]==x:
            return x
        p = self.find(self.parent[x])
        self.parent[x]=p
        return self.parent[x]

    def union(self, x,y):
        p1,p2=self.find(x),self.find(y)
        if p1!=p2:
            if self.rank[p1]<self.rank[p2]:
                p1,p2=p2,p1
            if self.rank[p1]==self.rank[p2]:
                self.rank[p1]+=1
            self.parent[p2]=p1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uni = unionClass(stones)
        for stone in stones:
            stone=tuple(stone)
            uni.union(stone[0],~stone[1])
        ans=set()
        for i,j in stones:
            ans.add(uni.find(i))
        return len(stones) - len(ans)