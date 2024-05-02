class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        ans = [1]*(rowIndex+1)
        a = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            ans[i] = a[i-1] + a[i]
        return ans