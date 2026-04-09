class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #null cases
        # solutions
        # current subset
        # do backtracking, and each time called, give it a smaller subset of
        # the numbers not used
        # the base case:
        # when the subset is equal to the target

        solutions = []
        candidates.sort()
        # curr = []

        def backtrack(idx, path, cur):
            if cur == target:
                solutions.append(path.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if cur + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1,path,cur + candidates[i])
                path.pop()
        backtrack(0,[],0)

        return solutions
