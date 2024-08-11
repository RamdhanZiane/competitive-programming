class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo=defaultdict(int)
        def solve(pos,s):
            if pos==len(nums):
                return int(target==s)
            if (pos,s) not in memo:
                memo[(pos,s)]+= solve(pos+1,s+nums[pos]) + solve(pos+1,s-nums[pos])
            return memo[(pos,s)]
        return solve(0,0)