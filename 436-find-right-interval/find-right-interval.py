class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        ind = {interval[0]:i for i,interval in enumerate(intervals)}
        intervals.sort(key=lambda x:x[0])
        ans = [None]*len(intervals)
        for i, (start, end) in enumerate(intervals):
            l,r = i, len(intervals)-1
            if start == end:
                ans[ind[start]] = ind[start]
                continue
            while l<=r:
                m = l + (r-l)//2
                if intervals[m][0]<end:
                    l = m+1
                else:
                    r = m-1
            if l<len(intervals) and r>=i:
                ans[ind[start]] = ind[intervals[l][0]]
            else:
                ans[ind[start]] = -1
        return ans