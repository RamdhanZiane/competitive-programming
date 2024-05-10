import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            carry = capacity
            num_days = 1
            for weight in weights:
                if weight>carry:
                    if num_days >= days:
                        return False
                    carry = capacity
                    num_days += 1
                carry -= weight
            return True
        l = max(weights)
        r = l*math.ceil((len(weights)/days))
        while l<=r:
            m = l + (r-l)//2
            if not valid(m):
                l = m+1
            else:
                r = m-1
        return l