class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 and (nums[0] + nums[1])== target:
            return [0,1]
        newdict = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in newdict:
                return [newdict[difference],i]
            newdict[n] = i