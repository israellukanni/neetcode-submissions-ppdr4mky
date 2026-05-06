class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        duppy = set()

        for n in nums:
            if n in duppy:
                return True
            duppy.add(n)
        return False