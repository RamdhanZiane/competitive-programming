class Solution:
    def splitString(self, s: str) -> bool:
        
        def bt(pos, prev):
            if pos==len(s):
                return True
            for i in range(pos, len(s)):
                cur=int(s[pos:i+1])
                if cur+1==prev and bt(i+1, cur):
                    return True
            return False


        for i in range(1,len(s)):
            if bt(i,int(s[:i])):
                return True
        return False