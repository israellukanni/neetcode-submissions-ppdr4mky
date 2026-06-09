class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        countlist = []
        for key,val in count.items():
            countlist.append((val,key))
        countlist.sort()

        return [val for key,val in countlist[-k:]]