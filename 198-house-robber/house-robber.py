class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        if len(nums)==1:
            return nums[0]
        def solve(i):
            if i<0:
                return 0
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[:2])
            if i not in memo:
                memo[i]=max(solve(i-1),solve(i-2)+nums[i])
            return memo[i]
        return solve(len(nums)-1)