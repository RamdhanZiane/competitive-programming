class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = list()
        cur = []
        cursum = 0
        def solve(k):
            nonlocal cursum
            if cursum>target:
                return
            elif cursum==target:
                ans.append(cur.copy())
            else:
                for i in range(k,len(candidates)):
                    cur.append(candidates[i])
                    cursum+=candidates[i]
                    solve(i)
                    cur.pop()
                    cursum-=candidates[i]
        solve(0)
        return list(ans)