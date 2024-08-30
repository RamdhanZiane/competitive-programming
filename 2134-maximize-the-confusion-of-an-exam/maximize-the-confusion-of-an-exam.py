class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n=len(answerKey)
        ans=0
        l,r=0,0
        pieces=k
        while r<n:
            while r<n and (pieces>0 or answerKey[r]=='T'):
                if answerKey[r]=='F':
                    pieces-=1
                r+=1
            ans=max(ans,r-l)
            while pieces==0:
                if answerKey[l]=='F':
                    pieces+=1
                l+=1
        l,r=0,0
        pieces=k
        while r<n:
            while r<n and (pieces>0 or answerKey[r]=='F'):
                if answerKey[r]=='T':
                    pieces-=1
                r+=1
            ans=max(ans,r-l)
            while pieces==0:
                if answerKey[l]=='T':
                    pieces+=1
                l+=1
            
        return ans