class Solution:
    def countBits(self, n: int) -> List[int]:
        return [Counter(bin(i)[2:])['1'] for i in range(n+1)]