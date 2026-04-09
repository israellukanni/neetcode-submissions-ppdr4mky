class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # null cases
        # 
        solution = []
        nums.sort()
        

        def backtrack(i, sub):
            solution.append(sub.copy())

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                sub.append(nums[j])
                backtrack(j+1,sub)
                sub.pop()
        backtrack(0,[])
        return solution
            



