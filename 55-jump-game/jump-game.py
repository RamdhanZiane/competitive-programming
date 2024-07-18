class Solution:
    def canJump(self, nums: List[int]) -> bool:
        capacity=0
        pos=0
        while pos<len(nums)-1:
            capacity=max(nums[pos],capacity-1)
            if capacity==0:
                return False
            pos+=1
        return True