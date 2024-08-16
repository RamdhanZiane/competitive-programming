class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        chmp=[poured]
        for i in range(query_row):
            tmp=[0 for _ in range(len(chmp)+1)]
            for j in range(len(chmp)):
                excess=(chmp[j]-1)/2
                if excess>0:
                    tmp[j]+=excess
                    tmp[j+1]+=excess
            chmp=tmp
        return min(1,chmp[query_glass])