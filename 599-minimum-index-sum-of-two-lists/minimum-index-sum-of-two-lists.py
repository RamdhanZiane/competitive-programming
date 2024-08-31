class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        best=float('inf')
        ans=[]
        for l1 in range(len(list1)):
            for l2 in range(len(list2)):
                if list1[l1]==list2[l2]:
                    if l1+l2<best:
                        best=l1+l2
                        ans=[]
                    if l1+l2==best:
                        ans.append(list1[l1])
        return ans