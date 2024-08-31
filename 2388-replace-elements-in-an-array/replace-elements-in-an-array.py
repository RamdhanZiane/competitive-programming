class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        fin_ops = {}
        n=len(operations)
        for i in range(n-1,-1,-1):
            k,v = operations[i]
            if v in fin_ops:
                fin_ops[k]=fin_ops[v]
            else:
                fin_ops[k]=v

        for i in range(len(nums)):
            if nums[i] in fin_ops:
                nums[i]=fin_ops[nums[i]]
        return nums