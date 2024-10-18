class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        if b%a==0:
            return a
        ans=1
        for i in range(2,int(min(a,b)//2+1)):
            if a%i==0 and b%i==0:
                ans=i
        return ans