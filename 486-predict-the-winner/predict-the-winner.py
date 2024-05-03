class Solution:

    def solve(self, nums, s,l,r, player):
        if l == r:
            return s+player*nums[l]
        r1 = self.solve(nums,s+player*nums[l],l+1,r,-player)
        r2 = self.solve(nums,s+player*nums[r],l,r-1,-player)
        if player > 0:
            return max(r1,r2)
        return min(r1,r2)

    def predictTheWinner(self, nums: List[int]) -> bool:
        a = self.solve(nums,0,0,len(nums)-1,1)
        print(a)
        return a >= 0