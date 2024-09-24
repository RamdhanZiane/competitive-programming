class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo={}

        i,j=0,len(piles)-1
        def solve(turn):
            nonlocal i
            nonlocal j
            if i>j:
                return 0
            if (i,j,turn) in memo:
                return memo[(i,j,turn)]
            i+=1
            a=solve(-turn)+turn*piles[i-1]
            i-=1
            j-=1
            b=solve(-turn)+turn*piles[j+1]
            j+=1
            
            if turn:
                memo[(i,j,turn)]=max(a,b)
            else:
                memo[(i,j,turn)]=min(a,b)
            return memo[(i,j,turn)]
        return solve(1)>0