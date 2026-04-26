class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0]*len(temperatures) 
        for i,temp in enumerate(temperatures):
            # print(stack,temp)
            while stack and temp > stack[-1][1]:
                tInd = stack.pop()[0]
                result[tInd] = i - tInd
            stack.append((i,temp))
            
        while stack:
            tInd = stack.pop()[0]
            result[tInd] = 0
        
        return result