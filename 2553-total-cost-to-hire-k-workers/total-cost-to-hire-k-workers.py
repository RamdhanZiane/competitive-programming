class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cand=[]
        left,right=0,len(costs)-1
        count=0
        while left<=right and count<candidates:
            heapq.heappush(cand,(costs[left],'l'))
            if left!=right:
                heapq.heappush(cand,(costs[right],'r'))
            left+=1
            right-=1
            count+=1
        ans=0
        for _ in range(k):
            cost,direc=heapq.heappop(cand)
            ans+=cost
            if direc=='l':
                if left<=right:
                    heapq.heappush(cand,(costs[left],'l'))
                    left+=1
            else:
                if left<=right:
                    heapq.heappush(cand,(costs[right],'r'))
                    right-=1
        return ans