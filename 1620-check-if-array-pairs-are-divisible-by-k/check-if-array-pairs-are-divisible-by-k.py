class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts=defaultdict(int)
        total=0
        for num in arr:
            r=num%k
            if counts[(k-r)%k]>0:
                counts[(k-r)%k]-=1
                total+=1
            else:
                counts[r]+=1
        return total==len(arr)//2