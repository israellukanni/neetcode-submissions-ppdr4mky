class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)
        prefix= 1
        for i,n in enumerate(nums):
            output[i] = prefix
            prefix *= n
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
