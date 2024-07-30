class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjacency=defaultdict(list)
        preq_count=[0]*numCourses
        not_dependant=set(range(numCourses))
        for a,b in prerequisites:
            if a in not_dependant:
                not_dependant.remove(a)
            preq_count[a]+=1
            adjacency[b].append(a)

        q=deque(not_dependant)
        ans=[]
        taken=set()
        while q:
            cur=q.popleft()
            ans.append(cur)
            for neigh in adjacency[cur]:
                preq_count[neigh]-=1
                if preq_count[neigh]==0:
                    q.append(neigh)
            
        if len(ans)==numCourses:
            return ans
        return []