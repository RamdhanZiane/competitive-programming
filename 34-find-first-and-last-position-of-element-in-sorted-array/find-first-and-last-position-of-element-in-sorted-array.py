import math
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(nums,target,mode):
            l, r, most = 0, len(nums)-1, -1
            while l<=r:
                m = (l+r)//2
                if nums[m]==target:
                    most = m
                    if mode == 'l':
                        r = m-1
                    else:
                        l = m+1
                elif nums[m]<target:
                    l = m+1
                else:
                    r = m-1
            return most
        return [find(nums,target,'l'), find(nums,target,'r')]