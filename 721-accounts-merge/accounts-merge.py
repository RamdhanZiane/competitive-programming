class union:
    def __init__(self):
        self.parent={}
        self.rank=defaultdict(int)
        self.name={}

    def find(self, x, name):
        p = self.parent.get(x,x)
        if p!=x:
            p = self.find(p, name)
        self.parent[x]=p
        self.name[x]=name
        return self.parent[x]

    def union(self, x, y, name):
        p1,p2 = self.find(x, name), self.find(y, name)
        if p1!=p2:
            if self.rank[p1]<self.rank[p2]:
                self.parent[p1]=p2
            else:
                if self.rank[p1]==self.rank[p2]:
                    self.rank[p1]+=1
                self.parent[p2]=p1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uni=union()
        for account in accounts:
            name=account[0]
            uni.find(account[1],name)
            for i in range(1,len(account)-1):
                uni.union(account[i], account[i+1], name)
        
        res = defaultdict(set)
        for k,v in uni.parent.items():
            res[uni.find(v, uni.name[k])].add(k)
        ans=[]
        for k,l in res.items():
            ans.append([uni.name[k]]+sorted(l))

        return ans