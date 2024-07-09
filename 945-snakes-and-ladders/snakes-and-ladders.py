class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        q=deque([1])
        visited=set([1])
        lvl=1
        def getposition(pos):
            q,r = divmod(pos - 1, n)
            row = n - 1 - q
            col = r if q % 2 == 0 else n - 1 - r
            return row,col
        while q:
            for _ in range(len(q)):
                cur=q.popleft()
                for i in range(1,7):
                    if cur+i not in visited:
                        visited.add(cur+i)
                        x,y=getposition(cur+i)
                        if board[x][y]!=-1:
                            if board[x][y]==n**2:
                                return lvl
                            q.append(board[x][y])
                        else:
                            if cur+i==n**2:
                                return lvl
                            q.append(cur+i)
            lvl+=1
        return -1