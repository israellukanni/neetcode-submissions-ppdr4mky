class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumMap = {}

        for i,n in enumerate(nums):

            if target - n in sumMap:
                return [sumMap[target-n],i]
            sumMap[n] = i
        