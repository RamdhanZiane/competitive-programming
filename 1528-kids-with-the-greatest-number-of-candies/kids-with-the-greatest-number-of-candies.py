class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        biggest=max(candies)
        for cand in candies:
            ans.append(cand+extraCandies>=biggest)
        return ans