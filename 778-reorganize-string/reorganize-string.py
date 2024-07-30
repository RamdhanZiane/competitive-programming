class Solution:
    def reorganizeString(self, s: str) -> str:
        
        hp=[]
        counts=Counter(s)
        for k,v in counts.items():
            heappush(hp,(-v,k))

        ans=[]
        tmp=None
        while hp:
            curc,curv = heappop(hp)
            curc+=1
            ans.append(curv)
            if tmp:
                heappush(hp,tmp)
            if curc<0:
                tmp=(curc,curv)
            else:
                tmp=None
        if len(ans)==len(s):
            return ''.join(ans)
        return ''