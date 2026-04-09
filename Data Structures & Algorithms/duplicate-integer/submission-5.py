class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashy = dict()

        for n in nums:
            if n in hashy:
                return True
            hashy[n] = 1
        return False