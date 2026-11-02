class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        inters = sorted(intervals)
        stack = []
        stack.append(inters[0])
        for s,e in inters[1:]:
            if stack[-1][1] >= s and stack[-1][1] >= e:
                continue
            elif stack[-1][1] >= s:
                stack[-1][1] = e
            else:
                stack.append([s,e])
        
        return stack
