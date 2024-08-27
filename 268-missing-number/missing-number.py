class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ans=sum(range(len(nums)+1))
        for i in nums:
            ans-=i
        return ans