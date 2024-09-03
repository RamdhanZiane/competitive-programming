class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xall=0
        for num in nums:
            xall^=num
        
        distinguish = xall&-xall

        a,b=0,0
        for num in nums:
            if num&distinguish==0:
                a^=num
            else:
                b^=num
        return [a,b]