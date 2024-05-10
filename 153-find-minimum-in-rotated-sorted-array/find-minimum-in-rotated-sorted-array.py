class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while True:
            if nums[l]>nums[r]:
                m = l+(r-l)//2
                if nums[m]<nums[l]:
                    r = m
                else:
                    l = m+1
            else:
                return nums[l]
        # return nums[m]