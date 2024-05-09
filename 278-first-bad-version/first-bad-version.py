# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        first_bad = n
        while l <= r:
            m = (r+l)//2
            if isBadVersion(m):
                first_bad = m
                r = m - 1
            else:
                l = m+1
        return first_bad