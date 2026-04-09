class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []

        def backtrack(arr, left):
            if len(sub) >= len(nums):
                res.append(sub.copy())
                return

            for i in range(len(left)):
                sub.append(left[i])
                backtrack(sub, left[:i]+left[i+1:])
                sub.pop()
        backtrack(sub,nums)
        return res