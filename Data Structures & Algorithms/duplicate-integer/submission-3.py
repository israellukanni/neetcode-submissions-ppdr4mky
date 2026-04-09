class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #o(n) time and space, meaning you can use an additional structure, but can only 
        # iterate "one" time thru
        if not nums:
            return False
        newDict = dict() # 1, 2, 3, 4
        for num in nums: 
            if num in newDict:
                return True
            newDict[num] = 1
        return False