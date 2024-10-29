class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts=Counter(words)
        hp=[]
        for c,v in counts.items():
            heapq.heappush(hp,(-v,c))
        ans=[]
        for _ in range(int(k)):
            ans.append(heapq.heappop(hp)[1])
        return ans