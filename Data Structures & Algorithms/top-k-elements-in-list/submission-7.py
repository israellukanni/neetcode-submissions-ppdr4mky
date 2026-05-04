class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hs = defaultdict(int)
        for n in nums:
            hs[n] +=1
        
        numsort = []
        for key,val in hs.items():
            numsort.append((val,key))
        numsort.sort()
        
        res = []
        while numsort and len(res)<k:
            res.append(numsort.pop()[1])
        return res