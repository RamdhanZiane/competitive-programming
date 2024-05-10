class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)*len(matrix[0])-1
        while l<=r:
            m = l + (r-l)//2
            i = m//len(matrix[0])
            j = m%len(matrix[0])
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                r = m-1
            else:
                l = l+1
        return False