class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target==1:
            return 0
        ans=0
        cur=target
        while cur!=1:
            if cur%2==1:
                cur-=1
            else:
                if maxDoubles>0:
                    maxDoubles-=1
                    cur/=2
                else:
                    return int(ans+(cur-1))
            ans+=1
        return ans