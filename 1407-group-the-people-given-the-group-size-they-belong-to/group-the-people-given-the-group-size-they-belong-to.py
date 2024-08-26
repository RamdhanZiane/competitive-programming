class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizes=defaultdict(list)
        for i,sz in enumerate(groupSizes):
            sizes[sz].append(i)
        ans=[]
        for k,v in sizes.items():
            i=0
            while i<len(v):
                ans.append(v[i:i+k])
                i+=k
        return ans