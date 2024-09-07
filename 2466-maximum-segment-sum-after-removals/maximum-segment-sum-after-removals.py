class unionClass:
    def __init__(self,n):
        self.parent={i:i for i in range(n)}
        self.rank=[0]*n
        self.sum=[0]*n
        self.best=0

    def find(self,x):
        if self.parent[x]==x:
            return x
        p = self.find(self.parent[x])
        self.parent[x]=p
        return self.parent[x]

    def union(self, x,y):
        p1,p2=self.parent[x],self.parent[y]
        if p1!=p2:
            self.parent[p2]=self.find(p1)
            self.sum[self.parent[p2]]+=self.sum[p2]
        


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n=len(nums)
        uni=unionClass(n)
        ans=[]
        for i in range(n-1,-1,-1):
            q=removeQueries[i]
            s=nums[q]
            ans.append(uni.best)
            uni.sum[q]+=nums[q]
            if q<n-1:
                uni.union(q+1,q)
            uni.best=max(uni.best, uni.sum[uni.find(q)])
        return reversed(ans)