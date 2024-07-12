class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total=0
        for i in range(len(piles)):
            total+=piles[i]
            piles[i]=-piles[i]
        heapq.heapify(piles)
        for _ in range(k):
            stones=-heapq.heappop(piles)
            if stones==1:
                break
            total-=stones//2
            heapq.heappush(piles, -stones+stones//2)
        return total