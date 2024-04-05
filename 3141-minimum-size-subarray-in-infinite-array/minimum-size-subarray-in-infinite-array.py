class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        left = right = 0
        n = len(nums)
        ans = math.inf
        arr_sum = sum(nums)
        ite = target // arr_sum
        sum_ = arr_sum * ite + nums[0]
        print(ite, sum_)
        while left < n:
            while sum_ < target:
                right += 1
                if right >= n:
                    right = 0
                    ite += 1
                sum_ += nums[right]
            while sum_ > target:
                sum_ -= nums[left]
                left += 1
                if left >= n:
                    break
            if sum_ == target:
                ans = min(ans, right - left + n*ite + 1)
                if left < n:
                    sum_ -= nums[left]
                    left += 1
        if ans != math.inf:
            return ans
        return -1