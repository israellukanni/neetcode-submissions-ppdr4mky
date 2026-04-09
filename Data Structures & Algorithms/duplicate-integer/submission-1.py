class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        newdict = {}
        for num in nums:
            if num in newdict:
                return True
            else:
                newdict[num] = 1
        return False