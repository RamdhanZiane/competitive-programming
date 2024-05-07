class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def S_n(n):
            if n == 1:
                return '0'
            prev = S_n(n-1)
            return prev + "1" + ''.join(map(lambda x:str(int(not bool(int(x)))), prev))[::-1]
        return S_n(n)[k-1]