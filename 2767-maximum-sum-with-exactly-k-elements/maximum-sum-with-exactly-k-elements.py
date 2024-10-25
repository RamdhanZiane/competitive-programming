class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return int(k*(2*max(nums)+k-1)/2)