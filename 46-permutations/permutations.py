class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(perm, indices):
            if len(perm)==len(nums):
                ans.append(perm)
                return
            for idx in indices:
                solve(perm+[nums[idx]],indices-{idx})
        ans = []
        solve([],set(range(len(nums))))
        return ans