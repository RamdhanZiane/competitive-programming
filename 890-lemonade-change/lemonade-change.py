class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change={
            10:0,
            5:0,
            20:0
        }
        for bill in bills:
            if bill==10:
                change[5]-=1
            if bill==20:
                if change[10]>0:
                    change[10]-=1
                else:
                    change[5]-=2
                change[5]-=1
            if change[5]<0:
                return False
            if change[10]<0:
                return False
            change[bill]+=1
                
        return True