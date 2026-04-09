class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashy = defaultdict(int)

        for n in nums:
            if n in hashy:
                return True
            hashy[n] +=1
        return False