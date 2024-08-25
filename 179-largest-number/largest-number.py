from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x,y):
            x,y=str(x),str(y)
            if x+y < y+x:
                return 1
            return -1
        nums.sort(key=cmp_to_key(cmp))
        if nums[0]==0:
            return '0'
        return ''.join(map(str,nums))