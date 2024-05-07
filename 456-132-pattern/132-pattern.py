import math
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        low_right = -math.inf
        stack = [nums[-1]]

        for num in list(reversed(nums))[1:]:
            if num < low_right:
                return True
            while stack and stack[-1] < num:
                low_right = stack.pop()
            stack.append(num)
        return False