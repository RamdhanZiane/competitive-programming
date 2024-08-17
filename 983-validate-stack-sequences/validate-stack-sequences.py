class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s=[]
        i=0
        for p in pushed:
            s.append(p)
            while s and i<len(popped) and popped[i]==s[-1]:
                s.pop()
                i+=1
        return i==len(popped) and len(s)==0