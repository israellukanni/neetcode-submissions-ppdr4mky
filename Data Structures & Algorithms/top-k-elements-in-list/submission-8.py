class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        kfreq = defaultdict(int)
        for n in nums:
            kfreq[n] += 1
        
        sortk = []
        for key,val in kfreq.items():
            sortk.append((val,key))
        sortk.sort()

        res = []
        while sortk and len(res) < k:
            res.append(sortk.pop()[1])
        return res
