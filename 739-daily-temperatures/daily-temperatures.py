class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        nexts = {}

        for i,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp :
                nexts[stack.pop()] = i
            nexts[i] = i
            stack.append(i)
        return  [nexts[i] - i for i,temp in enumerate(temperatures)]