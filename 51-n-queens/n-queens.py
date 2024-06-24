import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        cols=set()
        diag_right=set()
        diag_left=set()
        ans=[]
        queens=[]
        def verify(row,col):
            return not col in cols and not row-col in diag_right and not row+col in diag_left
        

        def backtrack(row):
            for col in range(n):

                if verify(row,col):
                    queens.append((row,col))
                    cols.add(col)
                    diag_right.add(row-col)
                    diag_left.add(row+col)
                    if row==n-1:
                        sol=[['.']*n for _ in range(n)]
                        for row,col in queens:
                            sol[row][col]='Q'
                        for row in range(n):
                            sol[row]=''.join(sol[row])
                        ans.append(sol)
                    else:
                        backtrack(row+1)
                    queens.pop()
                    cols.remove(col)
                    diag_right.remove(row-col)
                    diag_left.remove(row+col)
        backtrack(0)
        return ans