class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=defaultdict(int)
        for d in cpdomains:
            count,domain=d.split(' ')
            names=domain.split('.')
            for i in range(len(names)):
                ans['.'.join(names[i:])]+=int(count)
        return [' '.join([str(v),k]) for k,v in ans.items()]