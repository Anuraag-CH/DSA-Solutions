class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sub(nums,[])
        return self.result
    
    def sub(self,input,output):
        if len(input)==0:
            self.result.append(output)
            return
        ip = input[1:]
        op1 = output+([input[0]])
        op2 = output
        self.sub(ip,op1)
        self.sub(ip,op2)
    
#solution 2
# Path: recursion/subsets.py

class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sub(nums,0,[])
        return self.result
    
    def sub(self,input,index,output):
        if index==len(input):
            self.result.append(output)
            return
        op1 = output+([input[index]])
        op2 = output
        self.sub(input,index+1,op1)
        self.sub(input,index+1,op2)

#space complexity: O(n)
#time complexity: O(n*2^n)