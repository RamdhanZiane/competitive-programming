class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=[0,0]
        def expand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j-1
        for i in range(1,len(s)):
            x,y = expand(i,i)
            if y-x+1>ans[1]-ans[0]+1:
                ans=[x,y]
            x,y = expand(i-1,i)
            if y-x+1>ans[1]-ans[0]+1:
                ans=[x,y]
        return s[ans[0]:ans[1]+1]