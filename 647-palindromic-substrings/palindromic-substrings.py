class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def expand(i,j):
            res=0
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
                res+=1
            return res
        for i in range(len(s)):
            res = expand(i,i)
            if i>0:
                res+=expand(i-1,i)
            ans+=res
        return ans