from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        q1 = deque([0])
        q2 = deque([0])
        l = 0
        for r in range(1,len(nums)):
            while q1 and nums[q1[-1]] < nums[r]:
                q1.pop()
            q1.append(r)
            while q2 and nums[q2[-1]] > nums[r]:
                q2.pop()
            q2.append(r)
            while q1 and q2 and nums[q1[0]] - nums[q2[0]] > limit:
                if q1[0] == l:
                    q1.popleft()
                if q2[0] == l:
                    q2.popleft()
                l += 1
            ans = max(ans, r-l+1)
        return ans