class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        ans = 0
        total = 0

        while total < target:
            ans += 1
            total += ans
        
        while (total - target) % 2 != 0:
            ans += 1
            total += ans

        return ans