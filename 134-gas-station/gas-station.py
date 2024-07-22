class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans=0
        fuel=0
        necessary=0
        for i in range(len(gas)):
            fuel+=gas[i]-cost[i]
            if fuel<0:
                necessary-=fuel
                ans=i+1
                fuel=0
        if necessary<=fuel:
            return ans
        return -1