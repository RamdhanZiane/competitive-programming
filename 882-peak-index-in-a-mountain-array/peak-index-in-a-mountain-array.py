class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = -1,len(arr)
        while l+1<r:
            m = l + (r-l)//2
            if m == 0:
                return 1
            if m == len(arr)-1:
                return m-1
            if arr[m-1] < arr[m] > arr[m+1]:
                return m
            elif arr[m-1]<arr[m]:
                l = m
            else:
                r = m
        return r