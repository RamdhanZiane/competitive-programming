class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        qualWage=[(w,q) for w,q in zip(wage,quality)]
        qualWage.sort(key=lambda x:x[0]/x[1])
        qualq=[]
        total=0
        ans=float('inf')
        for w,q in qualWage:
            heapq.heappush(qualq,-q)
            total+=q
            if len(qualq)>k:
                total+=heapq.heappop(qualq)
            if len(qualq)==k:
                ans=min(ans,total*w/q)
        return ans