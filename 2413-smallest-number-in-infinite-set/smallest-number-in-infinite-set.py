class SmallestInfiniteSet:

    def __init__(self):
        self.hp=[1]
        self.check=1

    def popSmallest(self) -> int:
        res=heappop(self.hp)
        while self.hp and res==self.hp[0]:
            heappop(self.hp)
        if not self.hp:
            self.check+=1
            heappush(self.hp,self.check)
        return res

    def addBack(self, num: int) -> None:
        if num<self.check:
            heappush(self.hp,num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)