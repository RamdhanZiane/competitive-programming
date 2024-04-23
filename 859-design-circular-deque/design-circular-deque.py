class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k + 1
        self.deque = [None]*(k+1)
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        if self.head != (self.tail-1)%self.k:
            self.deque[self.tail] = value
            self.tail = (self.tail-1)%self.k
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if (self.head+1)%self.k != self.tail:
            self.head = (self.head+1)%self.k
            self.deque[self.head] = value
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail+1)%self.k
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head-1)%self.k
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[(self.tail+1)%self.k]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.head]

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def isFull(self) -> bool:
        return self.tail == (self.head+1)%self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()