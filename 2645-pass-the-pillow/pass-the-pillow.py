class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = time%(2*n-2)
        return r+1 if r<n else n-(r-(n-1))