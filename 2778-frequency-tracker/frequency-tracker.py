class FrequencyTracker:

    def __init__(self):
        self.nums=defaultdict(int)
        self.freqs=defaultdict(int)

    def add(self, number: int) -> None:
        if self.nums[number]>0:
            self.freqs[self.nums[number]]-=1
        self.nums[number]+=1
        self.freqs[self.nums[number]]+=1

    def deleteOne(self, number: int) -> None:
        if self.nums[number]>0:
            self.freqs[self.nums[number]]-=1
            self.nums[number]-=1
            if self.nums[number]>0:
                self.freqs[self.nums[number]]+=1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqs[frequency]>0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)