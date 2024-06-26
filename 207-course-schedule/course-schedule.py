class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency=defaultdict(set)
        courses=set()
        for u,v in prerequisites:
            adjacency[u].add(v)
            courses.add(u)
            courses.add(v)
        status = [0] * numCourses
        def has_cycle(course):
            if status[course] == 1:
                return True  
            if status[course] == 2:
                return False  
            status[course] = 1 
            for neighbor in adjacency[course]:
                if has_cycle(neighbor):
                    return True
            status[course] = 2
            return False

        for u in courses:
            if has_cycle(u):
                return False
        return True