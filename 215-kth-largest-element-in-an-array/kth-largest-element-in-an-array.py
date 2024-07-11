class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        largest=heapq.nlargest(k,nums)
        return largest[-1]