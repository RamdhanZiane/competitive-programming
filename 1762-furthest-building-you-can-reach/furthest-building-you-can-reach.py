class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        needed=[]
        for pos in range(len(heights)-1):
            if heights[pos+1]>heights[pos]:
                heapq.heappush(needed,heights[pos+1]-heights[pos])
                if len(needed)>ladders:
                    h=heapq.heappop(needed)
                    bricks-=h
                if bricks<0:
                    return pos
        return len(heights)-1