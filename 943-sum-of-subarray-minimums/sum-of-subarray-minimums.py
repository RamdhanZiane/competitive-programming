class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        left = defaultdict(lambda: -1)
        right = defaultdict(lambda: len(arr))
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 
        stack = [] 
        for i in range(len(arr) - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        return int(sum(((i - left[i]) * (right[i] - i) * value) % (1e9+7) for i, value in enumerate(arr))%(1e9+7))
      