class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adjacency=defaultdict(set)
        visited=set()
        q=deque([0])
        while q:
            cur=q.popleft()
            visited.add(cur)
            for neigh in rooms[cur]:
                if neigh not in visited:
                    q.append(neigh)
        return len(visited)==len(rooms)