class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modif=False
        n=len(nums)

        for i in range(1,n):
            if nums[i]<nums[i-1]:
                if modif: return False
                modif=True

                if i>1 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]

        return True