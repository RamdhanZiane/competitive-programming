from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.value = value
        self.k = k
        self.neg = 0

    def consec(self, num: int) -> bool:
        if len(self.stream) == self.k:
            popped = self.stream.popleft()
            if popped != self.value:
                self.neg -= 1
        self.stream.append(num)
        if num != self.value:
            self.neg += 1
        if len(self.stream) == self.k:
            return self.neg == 0
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)