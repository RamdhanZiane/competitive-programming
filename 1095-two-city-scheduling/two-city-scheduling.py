class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans=0
        costs.sort(key=lambda x:x[0]-x[1])
        for i in range(len(costs)//2):
            ans+=costs[i][0]+costs[i+len(costs)//2][1]
        return ans