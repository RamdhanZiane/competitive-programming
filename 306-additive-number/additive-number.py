class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        if len(num)<3:
            return False
        if num.count('0')==len(num):
            return True

        def bt(pos, pprev, prev):
            if pos==len(num):
                return True
            if num[pos]=='0':
                return False
            for i in range(pos, len(num)):
                cur=int(num[pos:i+1])
                if pprev+prev==cur and bt(i+1, prev, cur):
                    return True
            return False

        for i in range(1,len(num)):
            for j in range(i+1, len(num)):
                if bt(j, int(num[:i]), int(num[i:j])):
                    return True
                if num[i]=='0':
                    break
            if i==1 and num[0]=='0':
                break
        return False