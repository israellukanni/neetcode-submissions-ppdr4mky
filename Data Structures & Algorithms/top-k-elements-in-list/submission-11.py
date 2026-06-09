class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        countlist = []
        for key,val in count.items():
            countlist.append((val,key))
        countlist.sort()

        topk = []
        while len(topk) < k:
            topk.append(countlist.pop()[1])
        return topk