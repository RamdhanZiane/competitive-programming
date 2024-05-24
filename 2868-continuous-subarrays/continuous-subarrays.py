from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        maxq,minq = deque(),deque()
        start = ans = 0
        for end in range(len(nums)):
            while maxq and maxq[-1]<nums[end]:
                maxq.pop()
            maxq.append(nums[end])
            while minq and minq[-1]>nums[end]:
                minq.pop()
            minq.append(nums[end])

            while maxq[0] - minq[0] > 2:
                if nums[start] == maxq[0]:
                    maxq.popleft()
                if nums[start] == minq[0]:
                    minq.popleft()
                start += 1
            ans += end - start + 1
        return ans