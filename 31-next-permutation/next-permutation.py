class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i == -1:
            nums.reverse()
        else:
            pos = i+1
            for j in range(len(nums)-1, i, -1):
               if nums[j] > nums[i] and nums[j] < nums[pos]:
                   pos = j

            nums[i], nums[pos] = nums[pos], nums[i]
            nums[i+1:] = sorted(nums[i+1:])