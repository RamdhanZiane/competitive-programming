class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd = sum(nums[1::2])
        even = sum(nums[0::2])
        out = 0
        for idx in range(len(nums)):
            if idx%2 == 0:
                even -= nums[idx]
            else:
                odd -= nums[idx]

            if odd == even: out += 1
            
            if idx%2 == 0:
                odd += nums[idx]
            else:
                even += nums[idx]
        return out