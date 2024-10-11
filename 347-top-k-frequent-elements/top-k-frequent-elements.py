class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=Counter(nums)
        counts=sorted([(c,v) for c,v in counts.items()], key=lambda x:x[1], reverse=True)
        print(counts)
        ans=[]
        for i in range(k):
            ans.append(counts[i][0])
        return ans