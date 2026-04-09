class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #time : O(n*(2^n)) space: O(n) 
        res = []
        sub = []
        def backtrack(i):
            if i >= len(nums):
                res.append(sub.copy())
                return

            # for i in range(len(nums)):
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)

        backtrack(0)
        return res