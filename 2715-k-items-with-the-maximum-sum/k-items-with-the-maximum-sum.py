class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        for _ in range(k):
            if numOnes>0:
                ans+=1
                numOnes-=1
            elif numZeros>0:
                numZeros-=1
            else:
                ans-=1
                numZeros-=1
        return ans