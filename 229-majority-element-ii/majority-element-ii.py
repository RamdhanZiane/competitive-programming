class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp=defaultdict(int)
        for num in nums:
            mp[num]+=1
        ans=[]
        for k,v in mp.items():
            if v>len(nums)//3:
                ans.append(k)
        return ans