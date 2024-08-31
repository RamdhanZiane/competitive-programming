class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n
        
        balls=0
        dist=0
        for i in range(n):
            ans[i]+=dist
            balls+='1'==boxes[i]
            dist+=balls
        balls=0
        dist=0
        for i in range(n-1,-1,-1):
            ans[i]+=dist
            balls+='1'==boxes[i]
            dist+=balls

        return ans