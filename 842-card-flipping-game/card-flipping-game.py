class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        mp=defaultdict(bool)
        for i in range(len(fronts)):
            mp[fronts[i]] |= fronts[i]==backs[i]
            mp[backs[i]] |= fronts[i]==backs[i]
            
        for k in sorted(mp.keys()):
            if not mp[k]:
                return k
        return 0